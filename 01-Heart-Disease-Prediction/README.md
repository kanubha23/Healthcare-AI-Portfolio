# Clinical Prediction of Heart Disease Using Machine Learning


> **An end-to-end healthcare machine learning project comparing multiple supervised learning algorithms for predicting heart disease using clinical patient data.**

| Project Information | Details |
|--------------------|---------|
| **Project Type** | Supervised Machine Learning |
| **Domain** | Healthcare AI |
| **Task** | Binary Classification |
| **Dataset** | Clinical Heart Disease Dataset |
| **Models** | Logistic Regression, Decision Tree, Random Forest |
| **Best Model** | Logistic Regression |
| **Programming Language** | Python |
| **Libraries** | Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn |
---

##  Project Overview

Cardiovascular diseases remain one of the leading causes of mortality worldwide, making early detection essential for improving patient outcomes. Machine learning has the potential to support clinicians by identifying patients who may be at increased risk based on routinely collected clinical information.

In this project, three supervised machine learning algorithms were developed and compared to predict the presence of heart disease using clinical patient data. The complete machine learning workflow was implemented, including data exploration, preprocessing, model development, hyperparameter tuning, cross-validation, and model evaluation.

The primary objective was not only to build accurate predictive models but also to understand which clinical variables contribute most to heart disease prediction and evaluate the trade-off between predictive performance and model interpretability.

---

##  Project Objectives

The objectives of this project are to:

- Develop machine learning models capable of predicting the presence of heart disease.
- Compare the performance of multiple supervised learning algorithms.
- Evaluate models using clinically relevant performance metrics.
- Identify the most important clinical predictors of heart disease.
- Demonstrate a complete and reproducible machine learning workflow for healthcare data.

---

##  Research Questions

This project aims to answer the following research questions:

1. Can machine learning accurately predict the presence of heart disease?

2. Which supervised learning algorithm performs best on this dataset?

3. Which clinical variables contribute most to heart disease prediction?

4. Can interpretable machine learning models support clinical decision-making?

---

## Clinical Background

Heart disease remains one of the leading causes of death worldwide. Early diagnosis allows clinicians to initiate timely treatment and improve long-term patient outcomes.

Traditional diagnosis often requires multiple clinical examinations and specialist interpretation. Machine learning models have the potential to assist clinicians by analysing multiple patient characteristics simultaneously and estimating the likelihood of heart disease.

Although these models are not intended to replace clinical expertise, they can serve as valuable decision-support tools by identifying high-risk patients who may benefit from further investigation.


---

# Dataset

This project uses a publicly available clinical heart disease dataset containing demographic, physiological, and clinical measurements collected from patients undergoing cardiovascular assessment.

Each row represents a single patient, while each column corresponds to a clinical feature used for heart disease prediction.

### Target Variable

| Value | Description |
|------|-------------|
| 0 | No Heart Disease |
| 1 | Heart Disease |

### Clinical Features

| Feature | Description |
|----------|-------------|
| age | Age of the patient |
| sex | Biological sex |
| cp | Chest pain type |
| trestbps | Resting blood pressure |
| chol | Serum cholesterol |
| fbs | Fasting blood sugar |
| restecg | Resting electrocardiographic results |
| thalach | Maximum heart rate achieved |
| exang | Exercise-induced angina |
| oldpeak | ST depression induced by exercise |
| slope | Slope of the ST segment |
| ca | Number of major vessels |
| thal | Thalassemia status |

---

# Machine Learning Workflow

The project follows a complete end-to-end machine learning pipeline.

```text
Clinical Problem
        ↓
Dataset Loading
        ↓
Exploratory Data Analysis
        ↓
Data Preprocessing
        ↓
Train-Test Split
        ↓
Feature Scaling
        ↓
Model Development
        ↓
Model Evaluation
        ↓
Cross Validation
        ↓
Hyperparameter Tuning
        ↓
Feature Importance
        ↓
Model Comparison
        ↓
Discussion & Conclusions
```

---

# Machine Learning Models

Three supervised learning algorithms were implemented and compared.

## 1. Logistic Regression

A linear classification algorithm used as the baseline model.

### Advantages

- Fast to train
- Highly interpretable
- Produces probability estimates
- Well suited for binary classification

---

## 2. Decision Tree

A non-linear classification model that learns a sequence of decision rules from the data.

### Advantages

- Easy to visualize
- Captures non-linear relationships
- Requires little preprocessing

---

## 3. Random Forest

An ensemble learning algorithm that combines multiple Decision Trees using majority voting.

### Advantages

- Reduces overfitting
- More robust than a single Decision Tree
- Provides Feature Importance scores

---

# Model Performance

The three machine learning models were compared using Accuracy, Precision, Recall, and F1-score.

| Model | Accuracy | Precision | Recall | F1-score |
|--------|---------:|----------:|-------:|---------:|
| Logistic Regression | **0.900** | **0.875** | **0.875** | **0.875** |
| Decision Tree | 0.767 | 0.679 | 0.792 | 0.731 |
| Random Forest | 0.867 | 0.864 | 0.792 | 0.826 |

---

# Best Performing Model

Based on the evaluation metrics, **Logistic Regression** was selected as the final model.

### Why?

- Highest overall accuracy
- Highest precision
- Highest recall
- Highest F1-score
- Clinically interpretable
- Less complex than ensemble methods
- Suitable for healthcare decision support

Although Random Forest achieved strong predictive performance, it did not outperform Logistic Regression on this dataset.

---

# Repository Structure

```text
01-Heart-Disease-Prediction/
│
├── data/
│   └── heart.csv
│
├── notebooks/
│   └── Heart_Disease_Prediction.ipynb
│
├── images/
│   ├── correlation_heatmap.png
│   ├── roc_curve.png
│   ├── feature_importance.png
│   ├── logistic_confusion_matrix.png
│   ├── decision_tree_confusion_matrix.png
│   └── random_forest_confusion_matrix.png
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# Installation

Clone this repository:

```bash
git clone https://github.com/<kanubha23>/01-Heart-Disease-Prediction.git
```

Navigate to the project directory:

```bash
cd 01-Heart-Disease-Prediction
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

# How to Run the Project

1. Clone the repository.
2. Install the required dependencies.
3. Open the Jupyter Notebook:

```bash
jupyter notebook
```

4. Open:

```text
notebooks/Heart_Disease_Prediction.ipynb
```

5. Run the notebook from top to bottom.

---

# Skills Demonstrated

This project demonstrates the following technical skills:

### Programming

- Python
- Object-Oriented Programming
- Jupyter Notebook

### Data Analysis

- Pandas
- NumPy
- Exploratory Data Analysis (EDA)
- Data Visualization

### Machine Learning

- Data Preprocessing
- Train-Test Split
- Feature Scaling
- Logistic Regression
- Decision Tree
- Random Forest
- Hyperparameter Tuning
- GridSearchCV
- Cross-Validation
- ROC Curve Analysis
- Model Evaluation
- Feature Importance

### Healthcare AI

- Clinical Data Analysis
- Binary Disease Classification
- Model Interpretability
- Clinical Decision Support

---

# Future Improvements

Several extensions could further improve this project:

- Evaluate additional machine learning algorithms such as Support Vector Machines (SVM), XGBoost, and LightGBM.
- Incorporate additional clinical data, including laboratory biomarkers, ECG signals, cardiac imaging, and genomic information.
- Perform external validation using independent hospital datasets.
- Apply Explainable AI (XAI) techniques such as SHAP and LIME.
- Develop a web-based clinical decision support application using Streamlit or Flask.
- Investigate multimodal AI approaches by integrating structured clinical data with medical imaging and ECG signals.

---

# Key Learning Outcomes

This project provided practical experience with:

- End-to-end machine learning workflows
- Clinical data preprocessing
- Exploratory data analysis
- Supervised learning algorithms
- Hyperparameter optimization
- Model evaluation and comparison
- Scientific reporting
- Reproducible machine learning pipelines

---

# Acknowledgements

This project was developed as part of a personal Healthcare AI portfolio to strengthen practical skills in biomedical data science and machine learning.

The dataset used in this project is publicly available and is intended for educational and research purposes.

---

# License

This project is released under the MIT License.

See the `LICENSE` file for additional details.

---

# 👤 Author

**Kanubha Sharma**

MSc Medical Informatics

Biomedical Data Scientist | Healthcare AI | Clinical Machine Learning

LinkedIn: *(https://www.linkedin.com/in/kanubha-sharma-788a761bb/)*

GitHub: *(https://github.com/kanubha23)*