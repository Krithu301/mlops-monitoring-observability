from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Krithika’s A/B Testing Demo 💖"

@app.route('/predict')
def predict():
    # Randomly choose version A or B
    model_version = random.choice(['A', 'B'])

    if model_version == 'A':
        result = "Prediction from Model A 🅰"
    else:
        result = "Prediction from Model B 🅱"

    return f"{result} (You were served by Version {model_version})"

if __name__ == '__main__':
    app.run(port=8001)