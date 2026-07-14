# Diabetes Prediction using Machine Learning

> An end-to-end healthcare machine learning project for predicting diabetes using clinical data, featuring data preprocessing, machine learning pipelines, hyperparameter tuning, ROC-AUC analysis, and model explainability with SHAP.

---

## Project Overview

Diabetes is one of the most prevalent chronic diseases worldwide and early diagnosis is essential for preventing long-term complications such as cardiovascular disease, kidney failure, neuropathy, and vision loss.

The objective of this project is to develop and compare multiple machine learning models capable of predicting whether a patient has diabetes based on routinely collected clinical measurements.

This project demonstrates a complete machine learning workflow, from data exploration and preprocessing to model evaluation and explainable AI.

---

## Objectives

- Understand the clinical problem of diabetes prediction.
- Perform exploratory data analysis (EDA).
- Identify and handle missing values.
- Build reproducible preprocessing pipelines.
- Train and evaluate multiple machine learning models.
- Perform hyperparameter tuning using GridSearchCV.
- Compare model performance using multiple evaluation metrics.
- Evaluate models using ROC-AUC.
- Explain model predictions using SHAP.

---

## Dataset

**Dataset:** Pima Indians Diabetes Dataset

The dataset contains clinical measurements collected from female patients of Pima Indian heritage.

### Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target

- **0** → No Diabetes
- **1** → Diabetes

---

# Clinical Background

Diabetes mellitus is a chronic metabolic disorder characterized by elevated blood glucose levels resulting from impaired insulin production, insulin resistance, or both.

Early prediction enables timely intervention and can significantly reduce the risk of long-term complications.

Machine learning provides an opportunity to support clinicians by identifying high-risk patients using routinely collected clinical information.

---

# Project Workflow

```
Clinical Background
        │
        ▼
Data Exploration
        │
        ▼
Missing Value Handling
        │
        ▼
Train-Test Split
        │
        ▼
Machine Learning Pipelines
        │
        ▼
Model Training
        │
        ▼
Hyperparameter Tuning
        │
        ▼
Model Evaluation
        │
        ▼
ROC-AUC Analysis
        │
        ▼
SHAP Explainability
```

---

# Machine Learning Models

The following classification algorithms were implemented and compared:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)

---

# Data Preprocessing

The following preprocessing techniques were applied:

- Exploratory Data Analysis (EDA)
- Missing value identification
- Median imputation using `SimpleImputer`
- Feature scaling using `StandardScaler`
- Train-test split with stratification
- Machine learning pipelines using Scikit-learn

---

# Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC Curve
- Area Under the Curve (AUC)

---

# Hyperparameter Tuning

Hyperparameter optimization was performed using:

- GridSearchCV
- 5-Fold Cross Validation

This project demonstrates how hyperparameter tuning can improve model selection while highlighting that better cross-validation performance does not always guarantee improved performance on unseen test data.

---

# Explainable AI (SHAP)

Model predictions were interpreted using SHAP (SHapley Additive exPlanations).

The project includes:

- Global Feature Importance
- SHAP Summary Plot
- Local Patient-Level Explanation
- SHAP Waterfall Plot

These techniques improve model transparency and support trustworthy AI for healthcare applications.

---

# Repository Structure

```
02-Diabetes-Prediction
│
├── data/
│
├── notebooks/
│   └── Diabetes_Prediction.ipynb
│
├── figures/
│
├── README.md
│
└── requirements.txt
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SHAP
- Jupyter Notebook

---

# Machine Learning Concepts Covered

This project demonstrates practical implementation of:

- Exploratory Data Analysis (EDA)
- Missing Value Imputation
- Feature Scaling
- Train-Test Split
- Data Leakage Prevention
- Machine Learning Pipelines
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Hyperparameter Tuning
- GridSearchCV
- Cross Validation
- ROC Curve
- AUC
- SHAP Explainability

---

# Key Learning Outcomes

Through this project I learned how to:

- Build reproducible machine learning pipelines.
- Prevent data leakage during preprocessing.
- Compare multiple classification algorithms.
- Tune hyperparameters using cross-validation.
- Evaluate models using multiple performance metrics.
- Interpret machine learning predictions using Explainable AI (SHAP).
- Communicate machine learning results in a healthcare context.

---

# Future Improvements

Potential extensions include:

- Random Forest and Gradient Boosting models.
- XGBoost and LightGBM.
- Feature Selection techniques.
- Probability Calibration.
- Threshold Optimization.
- Deep Learning models.
- External validation on independent clinical datasets.

---

# Author

**Kanubha Sharma**

MSc Medical Informatics | Biomedical AI | Healthcare Data Science

This project is part of my **Healthcare AI Portfolio**, documenting my journey toward developing interpretable and clinically relevant AI solutions for healthcare.