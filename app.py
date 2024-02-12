from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and data
df = pd.read_csv('Cleaned_data.csv')
model = pickle.load(open('Model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    new_data = pd.DataFrame(data, index=[0])

    status = model.predict(new_data)

    return jsonify({'status': status.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
