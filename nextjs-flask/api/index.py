from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/interview/send_message")
def interview():
    return "<p>this is a response</p>"