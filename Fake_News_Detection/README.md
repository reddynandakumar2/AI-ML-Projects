# 📰 Fake News Detection using Machine Learning

## 📌 Project Overview

This project focuses on detecting whether a news article is **Fake** or **Real** using Natural Language Processing (NLP) and Machine Learning. The model analyzes the textual content of news articles, converts the text into numerical features, and predicts whether the news is genuine or misleading.

This project demonstrates the application of NLP techniques and supervised machine learning for binary text classification.

---

# 🎯 Problem Statement

The rapid spread of fake news on social media and online platforms can mislead people and influence public opinion. The objective of this project is to develop a machine learning model that automatically classifies news articles as **Fake** or **Real**, helping users identify unreliable information.

---

# 📂 Dataset

The dataset contains news articles labeled as:

* **Fake (0)** – False or misleading news articles.
* **Real (1)** – Genuine and verified news articles.

### Dataset Features

* **Title** – Headline of the news article.
* **Text** – Full news article content.
* **Subject** *(optional)* – News category.
* **Date** *(optional)* – Publication date.
* **Label** – Target variable (Fake or Real).

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Matplotlib
* Seaborn
* Joblib

---

# 📊 Data Preprocessing

The following preprocessing steps were applied:

* Removed missing values
* Converted text to lowercase
* Removed punctuation and special characters
* Removed stop words
* Tokenization
* Lemmatization
* TF-IDF Vectorization
* Train-Test Split

---

# 🔍 Feature Engineering

Text data was transformed into numerical features using:

* TF-IDF (Term Frequency–Inverse Document Frequency)

This representation helps the machine learning model identify important words and phrases that distinguish fake news from real news.

---

# 🤖 Machine Learning Models

The following classification models were evaluated:

* Logistic Regression
* Multinomial Naive Bayes
* Support Vector Machine (SVM)
* Random Forest Classifier
* Passive Aggressive Classifier

The best-performing model was selected based on evaluation metrics.

---

# 📈 Model Evaluation

The model performance was evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

# 📊 Project Workflow

```text
News Dataset
      │
      ▼
Text Cleaning
      │
      ▼
Tokenization & Lemmatization
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Fake / Real News Prediction
```

---

# 📁 Project Structure

```text
Fake-News-Detection/
│
├── dataset/
│   └── fake_news.csv
│
├── Fake_News_Detection.ipynb
└── README.md
```

---

# ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/Fake-News-Detection.git
```

### Navigate to the Project Folder

```bash
cd Fake-News-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train.py
```

### Predict News

```bash
python predict.py
```

---

# 🎯 Prediction Labels

| Label | Meaning   |
| ----: | --------- |
|     0 | Fake News |
|     1 | Real News |

---

# 📷 Sample Prediction

### Input

```text
Breaking News: Scientists discover a revolutionary AI system capable of diagnosing diseases with remarkable accuracy after extensive clinical testing.
```

### Output

```text
Prediction : Real News
Confidence : 97.8%
```

---

# 🚀 Future Improvements

* Integrate transformer-based models such as BERT or RoBERTa.
* Develop a real-time fake news detection web application using Streamlit or Flask.
* Support multilingual news classification.
* Add explainable AI techniques to interpret predictions.
* Deploy the model using cloud platforms.

---

# 💼 Skills Demonstrated

* Python Programming
* Natural Language Processing (NLP)
* Text Preprocessing
* TF-IDF Vectorization
* Machine Learning
* Binary Classification
* Feature Engineering
* Model Evaluation
* Scikit-learn
* Predictive Analytics

---

# 📄 License

This project is intended for educational purposes and portfolio demonstration.

---

# 👨‍💻 Author

**Petlo Nanda Kumar**

* AI & ML Engineer
* Machine Learning Enthusiast
* Natural Language Processing Developer
