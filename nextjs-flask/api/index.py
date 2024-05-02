from flask import Flask, request
import random

from deepmultilingualpunctuation import PunctuationModel as PuncModel


app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/interview/send_message", methods=["POST"])
def interview():
    data = request.get_json()
    print ('data: ', data)
    text = data.get('transcriptHistory')

    puncmodel = PuncModel()
    # text = "I've headache and feel irritation I've acidity but still feel hungry every time Got blurred vision and disturbances in vision I've pain in neck muscles and I feel depressed everytime"
    print('text: ',  text)
    result = str(puncmodel.restore_punctuation(text))
    print('punctuated: ',  result, type(result))

    splitted = result.split('.')
    splitted = [s.strip() for s in splitted if s.strip()]

    print('splitted: ', splitted, type(splitted))

    diagnosis = final_input(splitted)

    return ({'message': diagnosis})




# ============================================ ML MODEL BELOW ============================================


import torch
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler
from torch.utils.data import TensorDataset
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
import random
import time
import pandas as pd
import numpy as np
import random
import torch
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler, TensorDataset
from transformers import BertTokenizer, BertForSequenceClassification, RobertaTokenizer, RobertaForSequenceClassification, AdamW, get_linear_schedule_with_warmup
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tqdm.notebook import tqdm
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import hamming

import spacy


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

directory = './api/'

import pandas as pd
df = pd.read_excel(directory+'bert_training_data.xlsx')
df['user_defined_input'] = df['user_defined_input'].str.split('\n')

# Creating a new row for each description
df_exploded = df.explode('user_defined_input')
df = df_exploded
df['symptom'] = df['symptom'].str.strip()

class_counts = df['symptom'].value_counts()

# Define the minimum number of instances required per class
min_instances = 2

# Filter out classes with fewer than the minimum required number of instances
filtered_classes = class_counts[class_counts >= min_instances].index.tolist()

# Keep only the data with classes that meet the minimum instance criterion
df_filtered = df[df['symptom'].isin(filtered_classes)]

label_dict = {label: idx for idx, label in enumerate(df_filtered['symptom'].unique())}

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")


def process_text(text):
  doc = nlp(text)

  processed_text = " ".join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])
  return processed_text

tokenizer = RobertaTokenizer.from_pretrained('roberta-base', do_lower_case=True)

model = RobertaForSequenceClassification.from_pretrained(
    'roberta-base',
    num_labels=len(label_dict),
    output_attentions=False,
    output_hidden_states=False
)

# Load the model's state_dict
model.load_state_dict(torch.load(directory+'bert_finetuned.pth', map_location=device))
model.to(device)

def predict_top_symptoms(user_input, top_k=3):
    model.eval()
    user_input = process_text(user_input)
    encoded_input = tokenizer.encode_plus(
        user_input,
        add_special_tokens=True,
        return_attention_mask=True,
        padding='max_length',
        max_length=25,
        truncation=True,
        return_tensors='pt'
    ).to(device)


    # Perform the prediction
    with torch.no_grad():
        output = model(**{
            'input_ids': encoded_input['input_ids'],
            'attention_mask': encoded_input['attention_mask']
        })

    probs = torch.nn.functional.softmax(output.logits, dim=1)

    # Get the top k predicted classes and their probabilities
    top_probs, top_preds = torch.topk(probs, top_k)
    top_probs = top_probs.cpu().numpy()[0]
    top_preds = top_preds.cpu().numpy()[0]

    # Map the top predicted indices back to the symptom names
    top_symptoms = [list(label_dict.keys())[list(label_dict.values()).index(pred)] for pred in top_preds]

    # Combine the symptoms and their probabilities into a list of tuples
    top_symptoms_with_probs = list(zip(top_symptoms, top_probs))

    return top_symptoms_with_probs

data_w_disease = pd.read_csv(directory+'processed_data.csv')

data = data_w_disease.drop('Disease', axis=1)
data_rec = data.drop(columns=['user_id'])

col_in_data = data_rec.columns

def get_symptoms(top_symptoms_with_probs):
    temp_col = []
    max_value = 0
    max_symp = ''

    # Iterate over symptoms to find column names
    for symptom, value in top_symptoms_with_probs:
        if value >= 0.09:
            temp_col.append(symptom)
        elif value >= max_value:
            max_value = value
            max_symp = symptom

    if len(temp_col) == 0:
        temp_col.append(max_symp)

    return temp_col

def predict_symptoms(user_input):
    top_symptoms_with_probs = predict_top_symptoms(user_input, top_k=5)

    return get_symptoms(top_symptoms_with_probs)

df = pd.read_csv(directory+'DiseasePrecaution.csv')
df.replace("NaN", pd.NA, inplace=True)

precautions_dict = {row['Disease']: [value for value in row[1:] if pd.notna(value)] for index, row in df.iterrows()}

from collections import Counter

# INPUT: the list of user descriptions - one sentence for each symptom. The list user_inputs should have all the text provided by the user

def final_input(user_inputs):
  column_names = []

  for input in user_inputs:
      column_names += predict_symptoms(input)

  data_dict = {}

  for col_name in col_in_data:
    if col_name.strip() in column_names:
      data_dict[col_name] = 1
    else:
      data_dict[col_name] = 0
  user_symp = pd.DataFrame([data_dict])


  similarities = cosine_similarity(user_symp, data_rec)

  top_users_indices = np.argsort(similarities[0])[-10:][::-1]

  sim_user_diseases = [data_w_disease.iloc[d, 1] for d in top_users_indices]

  count = Counter(sim_user_diseases)

  # Find the most frequent disease
  diagnosis = count.most_common(1)[0][0]

  # three print statement variations
  statement_1 = f"Based on our findings, the diagnosis is {diagnosis}. To help manage your symptoms, we suggest you consider the following recommendations: {', '.join(precautions_dict[diagnosis])}. Please provide further details about your condition."
  statement_2 = f"After reviewing your case, we've determined that you have {diagnosis}. To help you feel better, we recommend that you: {', '.join(precautions_dict[diagnosis])}. Please provide further details about your condition."
  statement_3 = f"Our diagnosis indicates that you have {diagnosis}. To help alleviate your symptoms, we suggest you try the following: {', '.join(precautions_dict[diagnosis])}. Please provide further details about your condition."
  # List of the statements
  statements = [statement_1, statement_2, statement_3]
  # Randomly select and print one statement
  diagnosis_text = random.choice(statements)

#   diagnosis_text = "Final Diagnosis: " + str(diagnosis) + ". To alleviate your symptoms, we recommend: " + str(precautions_dict[diagnosis])
  print(diagnosis_text)

  return diagnosis_text


# UNCOMMENT TO TEST
# user_inputs = ["I've headache and feel irritation", "I've acidity but still feel hungry every time",
#                "Got blurred vision and disturbances in vision", "I've pain in neck muscles and I feel depressed everytime"]
# final_input(user_inputs)

# puncmodel = PuncModel()
# text = "I've headache and feel irritation I've acidity but still feel hungry every time Got blurred vision and disturbances in vision I've pain in neck muscles and I feel depressed everytime"
# print('text: ',  text)
# result = str(puncmodel.restore_punctuation(text))
# print('punctuated: ',  result, type(result))
# splitted = result.split('.')
# splitted = [s.strip() for s in splitted if s.strip()]
# print('splitted: ', splitted, type(splitted))
# final_input(splitted)

print ('====== FLASK SETUP FINISHED ======')
