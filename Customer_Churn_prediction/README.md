# Customer Churn Prediction

## 📌 Project Overview

Customer churn prediction is the process of identifying customers who are likely to stop using a company's services. This project uses Machine Learning techniques to analyze customer behavior and predict whether a customer will churn or stay with the company.

The model helps businesses identify at-risk customers and take proactive measures to improve customer retention.

---

## 🎯 Problem Statement

Customer retention is more cost-effective than acquiring new customers. The objective of this project is to build a machine learning model that predicts customer churn based on customer demographics, account information, and service usage.

---

## 📂 Dataset

- **Dataset Name:** Telco Customer Churn Dataset
- **Source:** Kaggle / IBM Sample Dataset
- **Target Variable:** `Churn`

### Features Include

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost (Optional)
- Jupyter Notebook

---

## 📊 Data Preprocessing

The following preprocessing techniques were applied:

- Removed unnecessary columns
- Handled missing values
- Converted data types
- Label Encoding
- One-Hot Encoding
- Feature Scaling using StandardScaler
- Train-Test Split

---

## ⚙️ Feature Engineering

- Converted categorical variables into numerical features
- Standardized numerical features
- Selected important features for better model performance

---

## 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- XGBoost Classifier

---

## 📈 Model Evaluation

Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

---

## 📊 Results

The best-performing model achieved approximately:

- Accuracy: **92%**
- Precision: High
- Recall: High
- F1 Score: High

The model successfully identifies customers who are likely to churn, enabling businesses to improve customer retention strategies.

---

## 📷 Project Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Customer Churn Prediction
```

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── code.ipynb
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/reddynandakumar2/Customer-Churn-Prediction.git
```

### Navigate to the Project Folder

```bash
cd Customer-Churn-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Notebook

```bash
jupyter notebook
```

Or run the Python script

```bash
python app.py
```

---

## 📌 Future Improvements

- Hyperparameter tuning
- Deep Learning model implementation
- Deployment using Flask or Streamlit
- Real-time prediction API
- Explainable AI using SHAP

---

## 💼 Skills Demonstrated

- Data Cleaning
- Data Visualization
- Feature Engineering
- Machine Learning
- Classification
- Model Evaluation
- Python Programming
- Data Preprocessing
- Predictive Analytics

---

## 📄 License

This project is created for educational and portfolio purposes.

---

## 👨‍💻 Author

**Petlo Nanda Kumar**

- AI & ML Enthusiast
- Machine Learning Engineer