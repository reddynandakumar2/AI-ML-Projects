# 🐶 Dogs vs Cats Image Classification using Deep Learning

## 📌 Project Overview

This project is a Deep Learning-based image classification system that accurately identifies whether an input image contains a **Dog** or a **Cat**. A Convolutional Neural Network (CNN) built with PyTorch is trained on labeled images to automatically learn visual features and classify them into one of the two categories.

This project demonstrates the application of Computer Vision and Deep Learning for binary image classification.

---

# 🎯 Problem Statement

Image classification is one of the most common tasks in computer vision. The objective of this project is to build a CNN model capable of distinguishing between dog and cat images with high accuracy, reducing the need for manual image categorization.

---

# 📂 Dataset

The dataset consists of two classes:

```text
dataset/
│
├── Cat/
└── Dog/
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
* Pillow (PIL)
* Scikit-learn

---

# 📊 Data Preprocessing

The following preprocessing steps were performed:

* Image resizing (128 × 128)
* Image normalization
* Conversion to PyTorch tensors
* Dataset loading using `ImageFolder`
* Data batching using `DataLoader`
* Train/Test split

---

# 🧠 Model Architecture

A Convolutional Neural Network (CNN) was implemented with:

* Convolutional Layers
* ReLU Activation
* Max Pooling Layers
* Fully Connected Layers
* Softmax Output Layer

The CNN automatically extracts important visual features from images and predicts whether the image is a **Dog** or a **Cat**.

---

# 📈 Model Evaluation

The model was evaluated using:

* Accuracy
* Loss
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

# 📊 Project Workflow

```text
Dataset
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
Dog/Cat Prediction
```

---

# 📁 Project Structure

```text
Dogs-vs-Cats-Classification/
│
├── dataset/
│   ├── Cat/
│   └── Dog/
│
├── models/
│   └── saved_model.pth
│
├── notebooks/
│   └── Dog_vs_Cat_Classification.ipynb
│
├── images/
│   └── sample_predictions.png
│
├── train.py
├── predict.py
├── requirements.txt
└── README.md
```

---

# ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/Dogs-vs-Cats-Classification.git
```

### Navigate to the Project Folder

```bash
cd Dogs-vs-Cats-Classification
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

| Class ID | Class |
| -------- | ----- |
| 0        | Cat   |
| 1        | Dog   |

---

# 📷 Sample Prediction

**Input Image**

```text
dog.jpg
```

**Prediction**

```text
Predicted Class : Dog
Confidence Score : 99.2%
```

---

# 🚀 Future Improvements

* Improve accuracy using transfer learning (ResNet50, EfficientNet, MobileNetV2)
* Apply data augmentation to improve generalization
* Build a Streamlit or Flask web application
* Deploy the model on cloud platforms
* Add support for multiple animal species

---

# 💼 Skills Demonstrated

* Python Programming
* Deep Learning
* Convolutional Neural Networks (CNN)
* PyTorch
* Computer Vision
* Image Classification
* Data Preprocessing
* Model Training
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
