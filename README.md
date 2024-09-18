# Employee Attrition Classification Model


Employee attrition is a critical challenge for many organizations. Predicting whether an employee will stay or leave can help businesses take proactive measures to improve retention and reduce turnover costs. This project focuses on building a machine learning model that classifies whether an employee is likely to stay or leave based on various features such as job satisfaction, performance rating, income, and more.

The project was developed in Python and deployed using Streamlit, with the primary goal of providing a user-friendly interface for predicting employee attrition.

## Problem Statement

The objective of this project is to develop a predictive model that accurately classifies employees into two categories: Stayed or Left, based on historical data. This model can assist human resource departments in identifying employees at risk of leaving the organization.

### Project Workflow

#### **Data Collection**

**Source Link:** https://www.kaggle.com/datasets/stealthtechnologies/employee-attrition-dataset

The dataset used for this project contains employee records with multiple features. Some of the key columns include:

Employee ID
Age
Gender
Years at Company
Job Role
Monthly Income
Work-Life Balance
Job Satisfaction
Performance Rating
Number of Promotions
Overtime
Distance from Home
Education Level
Number of Dependents
Job Level
Company Size
Remote Work
Leadership Opportunities
Innovation Opportunities
Company Reputation
Employee Recognition
Attrition (target variable)
2. Data Preprocessing
The following preprocessing steps were applied to prepare the data for machine learning:

Handling Missing Values: No missing values were present in the dataset.
Encoding Categorical Variables: Categorical columns like Gender, Overtime, Remote Work, and Job Role were encoded into numerical values using one-hot encoding.
Feature Scaling: Continuous variables such as Monthly Income, Years at Company, and Age were normalized to ensure they contribute equally to the model.
Feature Selection: Based on domain knowledge and exploratory data analysis, features with high impact on the target variable (attrition) were selected. These included Work-Life Balance, Job Satisfaction, Performance Rating, and Job Role.
3. Model Building
I experimented with different classification algorithms to find the best model for this task. The following models were trained:

Logistic Regression: A simple yet effective model for binary classification.
Random Forest Classifier: A robust, ensemble learning method that combines multiple decision trees.
XGBoost Classifier: An advanced gradient boosting technique known for its accuracy in classification tasks.
After evaluating the models using cross-validation and performance metrics such as accuracy, precision, recall, and F1 score, the XGBoost Classifier was chosen as the final model due to its superior performance.

4. Model Evaluation
The XGBoost model was evaluated on a holdout test set to ensure its generalization to unseen data. The following performance metrics were achieved:

Accuracy: 92%
Precision: 89%
Recall: 86%
F1-Score: 87%
These metrics demonstrate the model's ability to correctly classify employee attrition with a high degree of accuracy.

5. Saving the Model
The trained model was saved using joblib for deployment purposes. This allows for easy loading and usage of the model in the web application.

6. Application Development
The application was developed using Streamlit, an open-source framework for building interactive web applications in Python. The app allows users to input various employee features and receive a prediction on whether the employee is likely to stay or leave.

7. Application Deployment
The application was deployed successfully using Streamlit's cloud platform. Here are the key steps taken for deployment:

Step 1: Pushed the project files (including the Python script, saved model, and requirements.txt) to a GitHub repository.
Step 2: Created a requirements.txt file listing all the dependencies for the project, including streamlit, xgboost, and joblib.
Step 3: Set up the app's main file (attrition_app.py) which loads the trained model and builds the user interface for employee attrition prediction.
Step 4: Deployed the app via Streamlit's sharing platform, making it accessible for public use.
8. GitHub Repository
The GitHub repository for this project contains the following files:

attrition_app.py: The main Python script for running the Streamlit app.
xgb_model.pkl: The serialized XGBoost model.
requirements.txt: List of all required packages for the project.
README.md: A detailed description of the project.
9. Conclusion
This project successfully demonstrates how to build, train, and deploy a machine learning model for employee attrition prediction. The Streamlit app provides a simple and intuitive interface for users to interact with the model, allowing businesses to make informed decisions regarding employee retention strategies.

Next Steps
Model Improvement: Further hyperparameter tuning and experimentation with other algorithms (e.g., neural networks) could improve the model's accuracy.
Feature Engineering: Creating additional features from existing data, such as calculating tenure relative to job level, could provide more insights into attrition risk.
Integration: Integrating this app into a larger HR dashboard for real-time attrition prediction and analysis.
How to Access the App
You can access the deployed Streamlit app here. It is user-friendly and allows for easy interaction with the model.
