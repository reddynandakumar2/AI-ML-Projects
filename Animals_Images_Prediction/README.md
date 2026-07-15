# Animal Image Classification using Deep Learning

## 📌 Project Overview

This project is a deep learning-based image classification system that identifies an animal from an input image. The model is trained to classify images into one of the following five categories:

* 🦁 Lion
* 🐄 Cow
* 🐆 Leopard
* 🐅 Tiger
* 🐒 Monkey

The model uses a Convolutional Neural Network (CNN) built with PyTorch to automatically learn visual features from images and accurately predict the animal class.

---

# 🎯 Problem Statement

Manual identification of animals from images can be time-consuming and error-prone. The objective of this project is to develop a deep learning model capable of automatically recognizing different animal species from images with high accuracy.

---

# 📂 Dataset

The dataset consists of images belonging to five classes:

```
dataset/
│
├── Cow/
├── Lion/
├── Leopard/
├── Tiger/
└── Monkey/
```

Each folder contains images of the corresponding animal.

---

# 🛠️ Technologies Used

* Python
* PyTorch
* Torchvision
* NumPy
* Matplotlib
* OpenCV
* PIL (Python Imaging Library)
* Scikit-learn

---

# 📊 Data Preprocessing

The following preprocessing techniques were applied:

* Image resizing (128 × 128)
* Image normalization
* Tensor conversion
* Dataset loading using ImageFolder
* Data batching using DataLoader
* Train/Test split

---

# 🧠 Deep Learning Model

A Convolutional Neural Network (CNN) was implemented with the following architecture:

* Convolution Layers
* ReLU Activation
* Max Pooling Layers
* Fully Connected Layers
* Softmax Prediction

The network automatically extracts image features and classifies them into one of the five animal categories.

---

# 📈 Model Evaluation

The model was evaluated using:

* Accuracy
* Loss
* Confusion Matrix
* Classification Report
* Precision
* Recall
* F1-Score

---

# 📊 Project Workflow

```
Animal Images
      │
      ▼
Image Preprocessing
      │
      ▼
CNN Model Training
      │
      ▼
Model Validation
      │
      ▼
Model Testing
      │
      ▼
Animal Prediction
```

---

# 📁 Project Structure

```
Animal-Image-Classification/
│
├── dataset/
│   ├── Cow/
│   ├── Lion/
│   ├── Leopard/
│   ├── Tiger/
│   └── Monkey/
│
├── model/
│   └── savedmodel.pth
│
├── notebooks/
│   └── Animal_Classification.ipynb
│
├── images/
│   └── sample_predictions.png
│
├── predict.py
├── train.py
├── requirements.txt
└── README.md
```

---

# ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/Animal-Image-Classification.git
```

### Navigate to the Project

```bash
cd Animal-Image-Classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train.py
```

### Predict an Image

```bash
python predict.py
```

---

# 🎯 Prediction Classes

| Class ID | Animal  |
| -------- | ------- |
| 0        | Cow     |
| 1        | Lion    |
| 2        | Leopard |
| 3        | Tiger   |
| 4        | Monkey  |

---

# 📷 Sample Prediction

**Input Image**

```
lion.jpg
```

**Prediction**

```
Predicted Animal: Lion
Confidence: 98.6%
```

---

# 🚀 Future Improvements

* Add more animal classes
* Apply data augmentation for improved generalization
* Implement transfer learning using ResNet or EfficientNet
* Deploy the model using Streamlit or Flask
* Develop a web application for real-time image prediction

---

# 💼 Skills Demonstrated

* Python Programming
* Deep Learning
* Convolutional Neural Networks (CNN)
* PyTorch
* Computer Vision
* Image Preprocessing
* Model Training
* Image Classification
* Model Evaluation
* Predictive AI

---

# 📄 License

This project is intended for educational purposes and portfolio demonstration.

---

# 👨‍💻 Author

**Petlo Nanda Kumar**

* AI & ML Engineer
* Deep Learning Enthusiast
