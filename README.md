# Objective:
The objective of the project is to predict whether a startup which is currently `'Operating'`, `'IPO'`, `'Acquired'`, `'Closed'`. This problem will be solved through a Supervised Machine Learning approach by training a model based on the history of startups which were either acquired or closed. The data contains industry trends, investment insights and individual company information. Since the data was acquired on a trial basis, it only contains information about companies. After training the model, we predict the startups status. There are 44 columns out of which will be used as features. The rest provide more information about the data, but will not be used for model training (like normalized name, entity id, short description etc.)

# Pipeline through the project:

## 1. Data Collection:
Gathered relevant data for the predictive modeling task.

## 2. Data Exploration:
Explored the dataset to understand its structure, features, and relationships. Identified missing values, outliers, and potential data quality issues.

## 3. Data Preprocessing:
Handled missing data by imputation, removal, or other appropriate methods. Addressed outliers and anomalies to ensure data quality.
Converted categorical variables into numerical format through encoding techniques. Normalized numerical features to bring them to a consistent scale.

## 4. Feature Selection:
Assessed the importance of features to the target variable.
Employed techniques such as correlation analysis, recursive feature elimination, or feature importance from tree-based models.

## 5. Feature Engineering:
Created new features that might enhance the model's predictive power. Extracted meaningful information from existing features.
Handled date/time variables appropriately, considering features like last_funding_at, etc.

## 6. Model Building:
These sklearn models were used to make predicions on the startups status:

- Decision Tree Classifier
- XGBoost Classifier
- Random Forest Classifier
- Naive Bayes Classifier


## 7. Deployment :
## Model with Flask Integration Steps:

### Imported Required Libraries:
- Imported the Flask module for web application development.
- Imported necessary modules such as `render_template`, `request`, `pickle`, and `numpy`.

### Loaded Pretrained Model:
- Loaded the pretrained ensemble model using the `pickle` module.

### Created and Ran the Flask Application:
- Define Home Route:
  - Home Page Rendering: Designed the home page (`index.html`) with the necessary form for user input.
  - Created a route (`'/'`) that renders the home page (`index.html`).
- Define Prediction Route:
  - Created a route (`'/predict'`) that handles form submissions using the POST method.
- Extract Form Data:
  - Extracted input values from the form submitted by the user.
- Parse Input Data:
  - If needed, parsed input data to the appropriate data types (e.g., float or int).
- Prepare Input Data for Prediction:
  - Organized the input data into a numpy array to match the model's input format.
- Make Predictions:
  - Used the loaded ensemble model to make predictions on the input data.
- Render Result Page:
  - Displayed the prediction results on a separate result page (`result.html`).
