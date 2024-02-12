from flask import Flask, render_template, request
import pickle
import numpy as np  # Import numpy for array manipulation

# Load your pretrained model
ensemble_model = pickle.load(open("RandomForestClassifier.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    founded_at = float(request.form['founded_at'])  # Parse to float if needed
    first_funding_at = float(request.form['first_funding_at'])
    last_funding_at = float(request.form['last_funding_at'])
    funding_rounds = float(request.form['funding_rounds'])  # Parse to int if needed
    funding_total_usd = float(request.form['funding_total_usd'])
    first_milestone_at = float(request.form['first_milestone_at'])
    last_milestone_at = float(request.form['last_milestone_at'])
    milestones = float(request.form['milestones'])  # Parse to int if needed
    relationships = float(request.form['relationships'])  # Parse to int if needed

    # ... Repeat for other input fields ...
    # Prepare the input data for prediction
    input_data = np.array([[
        founded_at, first_funding_at, last_funding_at, funding_rounds, funding_total_usd,
        first_milestone_at, last_milestone_at, milestones, relationships
    ]])

    # Make predictions using the loaded model
    predictions = ensemble_model.predict(input_data)

    return render_template('result.html', prediction=predictions)

if __name__ == '__main__':
    app.run(debug=True)

