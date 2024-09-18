# Employee Attrition Classification Model

Employee attrition is a critical challenge for many organizations. Predicting whether an employee will stay or leave can help businesses take proactive measures to improve retention and reduce turnover costs. This project focuses on building a machine learning model that classifies whether an employee is likely to stay or leave based on various features such as job satisfaction, performance rating, income, and more.

The project was developed in Python and deployed using Streamlit, with the primary goal of providing a user-friendly interface for predicting employee attrition.

## Problem Statement

The objective of this project is to develop a predictive model that accurately classifies employees into two categories: Stayed or Left, based on historical data. This model can assist human resource departments in identifying employees at risk of leaving the organization.

### Project Workflow

#### **Data Collection**

**Source:** Kaggle
**Link:** https://t.ly/iD81A

The dataset used for this project contains employee records with multiple features. Some of the key columns include:


- Age
- Gender
- Years at Company
- Job Role
- Monthly Income
- Work-Life Balance
- Job Satisfaction
- Performance Rating
- Number of Promotions
- Overtime
- Distance from Home
- Education Level
- Number of Dependents
- Job Level
- Company Size
- Remote Work
- Leadership Opportunities
- Innovation Opportunities
- Company Reputation
- Employee Recognition
- _Attrition (target variable)_


### **Data Preprocessing**

The following preprocessing steps were applied to prepare the data for machine learning:

- **Handling Missing Values:**  I used the SimpleImputer to replace the missing value on the distance from home column with the mean.
  
- **Encoding Categorical Variables:** Categorical columns like Gender, Overtime, Remote Work, and Job Role were encoded into numerical values using one-hot encoding

- **Ordinal Encoder:** Ordered columns like Job Level, Company Size and Company Reputation were encoded into numerical values

- **Label Encoder:** The Attrition column which is the target variable was encoded into numerical values
  
- **Feature Scaling:**  - Continuous variables such as Years at Company, and Age were normalized to ensure they contribute equally to the model.
                        - The Monthly Income column was converted to groups to reduce cardinality
  
- **Feature Selection:** Based on domain knowledge and exploratory data analysis, features with high impact on the target variable (attrition) were selected. These included Work-Life Balance, Job Satisfaction, Performance Rating, and Job Role.


### **Model Building**

I experimented with different classification algorithms to find the best model for this task. The following models were trained:

- **Logistic Regression:** A simple yet effective model for binary classification.
- 
- **Random Forest Classifier:** A robust, ensemble learning method that combines multiple decision trees.
  
- **XGBoost Classifier:** An advanced gradient boosting technique known for its accuracy in classification tasks.
  
After evaluating the models using the model score and performance metrics such as accuracy, precision, recall, and F1 score, the XGBoost Classifier was chosen as the final model due to its superior performance.

- **Model Evaluation**
  
I evaluated the  XGBoost model to ensure its generalization to unseen data. The following performance metrics were achieved:

- Accuracy: 72%
- Precision: 73%
- Recall: 73%
- F1-Score: 73%
These metrics demonstrate the model's ability to correctly classify employee attrition with a high degree of accuracy.

### **Saving the Model**
The trained model was saved using joblib for deployment purposes. This allows for easy loading and usage of the model in the web application.

### **Application Development**
The application was developed using Streamlit, an open-source framework for building interactive web applications in Python. The app allows users to input various employee features and receive a prediction on whether the employee is likely to stay or leave.

### **Application Deployment**
The application was deployed successfully using Streamlit's cloud platform. Here are the key steps taken for deployment:

- Pushed the project files (including the Python script, saved model, and requirements.txt) to a GitHub repository.
  
- Created a requirements.txt file listing all the dependencies for the project, including streamlit, xgboost, and joblib.

- Set up the app's main file (attrition_app.py) which loads the trained model and builds the user interface for employee attrition prediction.
  
- Deployed the app via Streamlit's sharing platform, making it accessible for public use.
  
### **GitHub Repository**
The GitHub repository for this project contains the following files:

- attrition_app.py: The main Python script for running the Streamlit app.
- xgb_model.pkl: The serialized XGBoost model.
- requirements.txt: List of all required packages for the project.
- README.md: A detailed description of the project.

### **Conclusion**

This project successfully demonstrates how to build, train, and deploy a machine learning model for employee attrition prediction. The Streamlit app provides a simple and intuitive interface for users to interact with the model, allowing businesses to make informed decisions regarding employee retention strategies.

### **Next Steps**

**Model Improvement:** Further hyperparameter tuning and experimentation with other algorithms (e.g., neural networks) could improve the model's accuracy.

**Integration:** Integrating this app into a larger HR dashboard for real-time attrition prediction and analysis.

### **How to Access the App**
- You can access the deployed Streamlit app here https://t.ly/uWETi
- It is user-friendly and allows for easy interaction with the model.
- A user can choose the option that an employ has and click the predict option below the app and a prediction of whether the employee will stay or leav will appear

#### Thank you
