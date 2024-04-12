from flask import Flask
import random

app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/interview/send_message", methods=["POST"])
def interview():
    responses = [
        {'message': "Great to hear from you!"},
        {'message': "Thanks for reaching out."},
        {'message': "Interesting question! Let me think about it."},
        {'message': "I appreciate your inquiry."},
        {'message': "I'll get back to you as soon as possible."},
        {'message': "Sure thing, I'll look into it."},
        {'message': "Thanks for getting in touch!"},
        {'message': "I'll handle your request promptly."},
        {'message': "Let's discuss that further."},
        {'message': "I'm here to assist you."},
        {'message': "Certainly!"},
        {'message': "I'll address your query shortly."},
        {'message': "That's an intriguing topic!"},
        {'message': "I'm on it!"},
        {'message': "I'll provide you with an update soon."},
        {'message': "Thanks for bringing this to my attention."},
        {'message': "I'm here to help."},
        {'message': "Let's get started!"},
        {'message': "Absolutely."},
        {'message': "I'll make sure to respond promptly."},
    ]
    return random.choice(responses)

    # return {'message' : "this is a response"}