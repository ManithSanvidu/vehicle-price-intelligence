# 🚗 Vehicle Price Intelligence

### Machine Learning-Based Vehicle Pricing Decision Support

**IT3091 – Machine Learning | SLIIT**
**Group ID:** 2026-AI-03
**Track:** Industry Explorer
**Industry Partner:** Kangone Motor Traders

---

## 📌 Overview

**Vehicle Price Intelligence** is a machine learning project developed in collaboration with **Kangone Motor Traders**, a used-car dealership.

The project aims to develop a **vehicle price prediction model** using historical vehicle listing data to support pricing and trade-in decisions.

The dataset contains approximately **9,788 vehicle records** with attributes such as brand, model, year, mileage, engine capacity, transmission, fuel type, condition, features, location, and price.

---

## 🎯 Objectives

* Analyze historical vehicle listing data.
* Identify factors influencing vehicle prices.
* Develop a supervised regression model for price prediction.
* Compare multiple machine learning algorithms.
* Evaluate models using standard regression metrics.
* Provide data-driven pricing insights.

---

## 🤖 Machine Learning Approach

### Task

**Supervised Regression**

### Target

**Vehicle Price (LKR lakhs)**

### Initial Features

* Brand
* Model
* Year of Manufacture
* Engine Capacity
* Transmission
* Fuel Type
* Mileage
* Town
* Leasing Status
* Condition
* Vehicle Features

### Models

* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest
* XGBoost

### Evaluation Metrics

* RMSE
* MAE
* R²
* MAPE

---

## 🔄 Workflow

```text
Data Understanding
        ↓
EDA
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Model Development
        ↓
Cross-Validation & Tuning
        ↓
Model Evaluation
        ↓
Feature Importance
        ↓
Pricing Insights
```

---

## 📁 Project Structure

```text
vehicle-price-intelligence/
│
├── frontend/                         # User-facing web application
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── README.md
│
├── backend/                          # API for prediction
│   ├── app/
│   │   ├── routes/
│   │   │   └── prediction.py
│   │   ├── services/
│   │   │   └── prediction_service.py
│   │   ├── schemas/
│   │   │   └── vehicle.py
│   │   ├── main.py
│   │   └── config.py
│   ├── requirements.txt
│   └── README.md
│
├── data/
│   ├── raw/                          # Original stakeholder data
│   └── processed/                    # Cleaned/transformed data
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_data_cleaning.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_baseline_models.ipynb
│   ├── 06_advanced_models.ipynb
│   └── 07_model_evaluation.ipynb
│
├── src/
│   ├── data/
│   │   ├── loading.py
│   │   ├── cleaning.py
│   │   └── validation.py
│   │
│   ├── features/
│   │   ├── engineering.py
│   │   └── encoding.py
│   │
│   ├── models/
│   │   ├── linear_regression.py
│   │   ├── ridge.py
│   │   ├── lasso.py
│   │   ├── random_forest.py
│   │   └── xgboost_model.py
│   │
│   ├── evaluation/
│   │   ├── metrics.py
│   │   ├── cross_validation.py
│   │   └── model_comparison.py
│   │
│   └── visualization/
│       └── plots.py
│
├── models/                           # Saved trained models
│   ├── preprocessing/
│   └── trained/
│
├── reports/
│   ├── figures/
│   ├── tables/
│   ├── data-dictionary.md
│   └── decision-log.md
│
├── tests/
│   ├── test_data.py
│   ├── test_features.py
│   ├── test_models.py
│   └── test_api.py
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## 👥 Team

| Student ID | Member              | Responsibility                       |
| ---------- | ------------------- | ------------------------------------ |
| IT24101458 | Sanvidu M.G.M.      | Data Understanding & EDA             |
| IT24101408 | Gunawardana D.W.    | Data Cleaning & Preprocessing        |
| IT24101021 | Fernando U.D.U.     | Feature Engineering & Initial Models |
| IT24100111 | Somawantha M.H.K.C. | Advanced Models & Evaluation         |

All major methodological decisions, model comparisons, documentation, and final recommendations are reviewed collaboratively.

---

## 🛠️ Technology Stack

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **XGBoost**
* **Matplotlib**
* **Seaborn**
* **Jupyter Notebook**
* **Git & GitHub**

---

## ⚠️ Scope

The project focuses on **used-vehicle price estimation and price-influencing factors**.

Long-term market-wide price and demand forecasting are outside the scope due to the limited historical time period of the available dataset.

---

## 🔐 Data Privacy

The vehicle dataset was provided by the industry stakeholder for academic purposes. Confidential or restricted stakeholder data should not be committed to the public repository.

---

### 🎓 IT3091 – Machine Learning

**Sri Lanka Institute of Information Technology (SLIIT)**
**Group 2026-AI-03**

> *Turning vehicle data into data-driven pricing insights.*
