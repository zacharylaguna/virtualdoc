# VirtualDoc

VirtualDoc is a web application designed to provide virtual assistance similar to a remote doctor. With VirtualDoc, users can simply speak into the microphone, describing their symptoms as they would to a doctor, and the application will analyze the symptoms and output potential causes and remedies.

## Features

- **Speech-to-Text Input:** Users can speak into the microphone, describing their symptoms, and VirtualDoc will convert their speech into text for analysis.
- **Symptom Analysis:** The application analyzes the symptoms provided by the user and generates potential causes and remedies based on the analysis.
- **Interactive Interface:** Users can interact with the application through a user-friendly interface, where they can input their symptoms and view the analysis results.
- **Next.js and Flask Integration:** VirtualDoc utilizes Next.js for the frontend and Flask for the backend, providing a seamless integration between the two technologies.
  
## Getting Started

To get started with VirtualDoc, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/zacharylaguna/virtualdoc.git
    ```

2. Navigate to the project directory:

    ```bash
    cd VirtualDoc
    ```

3. Install the dependencies for both the frontend and backend:

    ```bash
    cd frontend
    npm install

    cd ../backend
    pip install -r requirements.txt
    ```

4. Start the Next.js frontend server:

    ```bash
    cd ../frontend
    npm run dev
    ```

5. Start the Flask backend server:

    ```bash
    cd ../backend
    python app.py
    ```

6. Open your web browser and navigate to `http://localhost:3000` to access VirtualDoc.

## Technologies Used

- **Next.js:** Next.js is a React framework that enables server-side rendering and other powerful features for building web applications.
- **Flask:** Flask is a lightweight WSGI web application framework in Python, perfect for building web APIs and backend services.
- **SpeechRecognition API:** VirtualDoc utilizes the SpeechRecognition API to convert speech to text input.
- **Natural Language Processing (NLP):** NLP techniques are employed to analyze the symptoms provided by the user and generate potential causes and remedies.

## Contributors

- [Zachary Laguna](https://github.com/zacharylaguna)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the developers of Next.js and Flask for creating such powerful frameworks.
- Special thanks to the SpeechRecognition API developers for enabling speech-to-text functionality.
- Inspired by the idea of leveraging technology to provide virtual medical assistance.

