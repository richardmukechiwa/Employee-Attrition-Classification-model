import streamlit as st
import joblib
import numpy as np

# Load your trained model using joblib
model = joblib.load('xgb_model.pkl')

# Function to predict attrition
def predict_attrition(features):
    # Convert features to a 2D array for the model
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    return 'Leave' if prediction[0] == 1 else 'Stay'

# Streamlit application
def main():
    st.title("Employee Attrition Prediction App")

    # Feature inputs from user
    age = st.slider('Age', 18, 65, 30)
    years_at_company = st.slider('Years at Company', 0, 40, 5)
    work_life_balance = st.selectbox('Work-Life Balance', [1, 2, 3, 4], format_func=lambda x: ['Poor', 'Fair', 'Good', 'Excellent'][x-1])
    job_satisfaction = st.selectbox('Job Satisfaction', [1, 2, 3, 4], format_func=lambda x: ['Low', 'Medium', 'High', 'Very High'][x-1])
    performance_rating = st.selectbox('Performance Rating', [1, 2, 3, 4], format_func=lambda x: ['Below Average', 'Average', 'High', 'Very High'][x-1])
    num_promotions = st.slider('Number of Promotions', 0, 10, 0)
    distance_from_home = st.slider('Distance from Home (km)', 0, 100, 10)
    education_level = st.selectbox('Education Level', [1, 2, 3, 4, 5], format_func=lambda x: ['High School', 'Associate Degree', 'Bachelor’s Degree', 'Master’s Degree', 'Doctorate'][x-1])
    num_dependents = st.slider('Number of Dependents', 0, 5, 0)
    job_level = st.selectbox('Job Level', [1, 2, 3, 4, 5], format_func=lambda x: ['Entry', 'Mid', 'Senior', 'Lead', 'Executive'][x-1])
    company_size = st.selectbox('Company Size', [1, 2, 3], format_func=lambda x: ['Small', 'Medium', 'Large'][x-1])
    company_reputation = st.selectbox('Company Reputation', [1, 2, 3, 4], format_func=lambda x: ['Poor', 'Fair', 'Good', 'Excellent'][x-1])
    employee_recognition = st.selectbox('Employee Recognition', [1, 2, 3], format_func=lambda x: ['Low', 'Medium', 'High'][x-1])
    monthly_income = st.slider('Monthly Income', 1000, 20000, 5000)

    # Encoded categorical features
    gender = st.radio("Gender", ('Male', 'Female'))
    overtime = st.radio("Overtime", ('Yes', 'No'))
    remote_work = st.radio("Remote Work", ('Yes', 'No'))
    leadership_opportunities = st.radio("Leadership Opportunities", ('Yes', 'No'))
    innovation_opportunities = st.radio("Innovation Opportunities", ('Yes', 'No'))

    # Job Role One-Hot Encoding
    job_role = st.selectbox('Job Role', ['Education', 'Finance', 'Healthcare', 'Media', 'Technology'])

    # Feature engineering (manually encoding categorical variables)
    gender_male = 1 if gender == 'Male' else 0
    gender_female = 1 if gender == 'Female' else 0
    overtime_yes = 1 if overtime == 'Yes' else 0
    overtime_no = 1 if overtime == 'No' else 0
    remote_work_yes = 1 if remote_work == 'Yes' else 0
    remote_work_no = 1 if remote_work == 'No' else 0
    leadership_yes = 1 if leadership_opportunities == 'Yes' else 0
    leadership_no = 1 if leadership_opportunities == 'No' else 0
    innovation_yes = 1 if innovation_opportunities == 'Yes' else 0
    innovation_no = 1 if innovation_opportunities == 'No' else 0

    job_role_encoded = {
        'Job Role_Education': 0,
        'Job Role_Finance': 0,
        'Job Role_Healthcare': 0,
        'Job Role_Media': 0,
        'Job Role_Technology': 0
    }
    job_role_encoded[f'Job Role_{job_role}'] = 1

    # Collect all feature inputs into an array
    features = [
        age, years_at_company, work_life_balance, job_satisfaction, performance_rating,
        num_promotions, distance_from_home, education_level, num_dependents, job_level,
        company_size, company_reputation, employee_recognition, monthly_income,
        gender_female, gender_male, overtime_no, overtime_yes, remote_work_no, remote_work_yes,
        leadership_no, leadership_yes, innovation_no, innovation_yes,
        job_role_encoded['Job Role_Education'], job_role_encoded['Job Role_Finance'],
        job_role_encoded['Job Role_Healthcare'], job_role_encoded['Job Role_Media'],
        job_role_encoded['Job Role_Technology']
    ]

    # Prediction
    if st.button('Predict'):
        result = predict_attrition(features)
        st.success(f'The employee is likely to: {result}')

# Run the application
if __name__ == '__main__':
    main()
