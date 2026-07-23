# Breast Cancer Diagnosis using Machine Learning

## Project Overview

This project explores the application of classical machine learning techniques for breast cancer diagnosis using the Breast Cancer Wisconsin Diagnostic Dataset.

The objective is to develop predictive models capable of classifying tumors as **benign** or **malignant**, while also understanding **why** the models make their predictions through Explainable AI (XAI).

Rather than focusing only on model accuracy, this project emphasizes model interpretability, feature selection, and clinical relevance, making it suitable for healthcare AI applications.

---
## Key Takeaways

- Built and compared three machine learning models for breast cancer diagnosis.
- Achieved **96.49% accuracy** using Logistic Regression.
- Applied four feature selection techniques to identify clinically relevant biomarkers.
- Compared model performance using Accuracy, Precision, Recall, F1-score, ROC-AUC, and Confusion Matrix.
- Used SHAP (Explainable AI) to interpret both global model behavior and individual patient predictions.

## Project Objectives

- Understand the clinical background of breast cancer diagnosis.
- Perform exploratory data analysis (EDA).
- Apply multiple feature selection techniques.
- Train and compare different machine learning models.
- Evaluate model performance using standard classification metrics.
- Interpret model predictions using Explainable AI (SHAP).

---

## Dataset

**Dataset:** Breast Cancer Wisconsin Diagnostic Dataset

- **Samples:** 569
- **Features:** 30 numerical features extracted from digitized images of breast cell nuclei
- **Target Classes:**
  - Malignant (0)
  - Benign (1)

The dataset contains measurements describing characteristics such as:

- Radius
- Texture
- Perimeter
- Area
- Smoothness
- Concavity
- Concave Points
- Symmetry
- Fractal Dimension

---

## Exploratory Data Analysis

The following analyses were performed:

- Dataset exploration
- Missing value inspection
- Class distribution analysis
- Statistical summary
- Correlation analysis
- Pairplot visualization
- Correlation heatmap

---

## Feature Selection Techniques

Multiple feature selection approaches were compared:

- Variance Threshold
- SelectKBest
- Recursive Feature Elimination (RFE)
- Random Forest Feature Importance

The agreement between these techniques helped identify the most informative biomarkers for breast cancer classification.

---

## Machine Learning Models

Three supervised machine learning models were implemented and compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest

---

## Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report
- ROC Curve
- Area Under the Curve (AUC)

### Model Performance

| Model | Accuracy | AUC |
|--------|---------:|----:|
| Logistic Regression | **96.49%** | **≈0.997** |
| Decision Tree | 91.23% | 0.9157 |
| Random Forest | 95.61% | 0.9937 |

Among the evaluated models, **Logistic Regression** achieved the best overall performance on this dataset.

---

## Explainable AI (XAI)

To improve model interpretability, SHAP (SHapley Additive exPlanations) was used to explain both:

- Global feature importance
- Individual patient predictions

This provides greater transparency and helps understand which clinical features influenced the model's decisions.

---

## Key Findings

- Logistic Regression achieved the highest overall performance despite being the simplest model.
- Random Forest produced competitive results while offering feature importance for model interpretation.
- Decision Tree showed lower generalization performance due to overfitting.
- Features related to **tumor size** and **boundary irregularity** were consistently identified as the most important predictors.
- SHAP explanations demonstrated that the model relied on clinically meaningful characteristics when making predictions.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SHAP

---

## Project Structure

```
Breast-Cancer-Diagnosis/
│
├── notebook/
│   └── breast_cancer_diagnosis.ipynb
│
├── figures/
│   ├── correlation_heatmap.png
│   ├── roc_curve_logistic_regression.png
│   ├── roc_curve_decision_tree.png
│   ├── roc_curve_random_forest.png
│   ├── random_forest_feature_importance.png
│   ├── shap_summary_plot.png
│   └── ...
│
├── results/
│   └── random_forest_feature_importance.csv
│
└── README.md
```

---

## Skills Demonstrated

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Feature selection
- Supervised Machine Learning
- Model comparison
- Performance evaluation
- Explainable AI (SHAP)
- Clinical interpretation of AI models

---

## Future Improvements

Possible extensions of this project include:

- Hyperparameter tuning using GridSearchCV or RandomizedSearchCV.
- Cross-validation for more robust performance estimation.
- Ensemble model comparison using XGBoost or LightGBM.
- Calibration analysis for probability estimation.
- Deployment of the trained model as a web application using Streamlit.

---

## About Me

I am a Medical Informatics graduate passionate about applying Artificial Intelligence and Machine Learning to solve real-world healthcare challenges.

This project is part of my **Healthcare AI Portfolio**, where I build end-to-end machine learning and deep learning projects focused on biomedical data, explainable AI, and clinical decision support systems.