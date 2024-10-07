# Employee Attrition Classification Model

Employee attrition is a critical challenge for many organizations. Predicting whether an employee will stay or leave can help businesses take proactive measures to improve retention and reduce turnover costs. This project focuses on building a machine learning model that classifies whether an employee is likely to stay or leave based on various features such as job satisfaction, performance rating, income, and more.

## Objective

The objective of this project is to develop a predictive model that accurately classifies employees into two categories: Stayed or Left, based on historical data. This model can assist human resource departments in identifying employees at risk of leaving the organization.

### Project Workflow

#### **Data Collection**

**Source:** Kaggle
**Link:** https://www.kaggle.com/datasets/stealthtechnologies/employee-attrition-dataset

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
  
- **Feature Selection:** Based on domain knowledge and exploratory data analysis, features with high impact on the target variable (attrition) were selected. These included Work-Life Balance, Job Level, Number of promotions, Gender and Remote Working option.

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

### **Insights**

**Higher Attrition Among Younger Employees**

- Employees under the age of 30 show a significantly higher likelihood of leaving the organization. This suggests that future talent is at risk of being lost.

**Recommendation:** Implement targeted retention strategies, such as clear career development plans and mentorship opportunities, to engage and retain younger employees.

**Non-Remote Workers are More Likely to Leave**

- Non-remote employees exhibit higher attrition rates compared to their remote counterparts.

**Recommendation:** Consider a balanced approach to remote and non-remote work to accommodate diverse work preferences and reduce potential turnover.

**Key Influencers:** - Job Level, Remote Work, Gender, and Work-Life Balance
  
- Factors such as job level, the ability to work remotely, gender, and work-life balance have a pronounced impact on employee attrition.

**Job Level:** - Engage junior-level employees in strategic initiatives to increase their sense of inclusion and respect within the organization.
  
**Gender:** - Attrition rates are notably higher among women, highlighting a need to investigate gender-related concerns, including career advancement and work-life balance.

**Work-Life Balance:** - Prioritize work-life balance through initiatives such as flexible scheduling, staff rotations, and structured vacation policies to mitigate attrition risks.

### **Conclusion**

This project successfully demonstrates how to build  and  train  an employee attrition prediction model 

### **Next Steps**

**Model Improvement:** Further hyperparameter tuning and experimentation with other algorithms (e.g., neural networks) could improve the model's accuracy.




