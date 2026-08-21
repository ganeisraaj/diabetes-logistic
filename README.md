# Thema 4 — Logistic Regression for Diabetes Prediction
**Logistische Regression zur Vorhersage von Diabetes**
**Technische Universität Dortmund | Department of Statistics | SoSe 2026**
Supervised by Prof. Dr. Katja Ickstadt, JProf. Dr. Nils Weitzel, Dr. Zeyu Ding
Author: Ganeisraaj Kathiravan | Group partner: Jakub Marczak

---

## 🚀 Live App / Live-Anwendung

An interactive Streamlit app based on this analysis is deployed here:

👉 **[Diabetes Risk Predictor — Live App](https://ganeisraaj-diabetes-logistic.streamlit.app/)**

Input patient values and get a real-time diabetes probability estimate.

---

## Overview / Überblick

This project applies binary logistic regression to predict diabetes diagnosis in a sample of female patients from the Pima Indian community. The analysis includes complete separation detection, model diagnostics, odds ratio interpretation, and classification performance evaluation via ROC curve and AUC.

Dieses Projekt wendet binäre logistische Regression an, um die Diabetesdiagnose in einer Stichprobe weiblicher Patientinnen der Pima-Indianer vorherzusagen. Die Analyse umfasst die Erkennung vollständiger Separation, Modelldiagnostik, Odds-Ratio-Interpretation sowie die Bewertung der Klassifikationsleistung mittels ROC-Kurve und AUC.

---

## Data / Daten

| | |
|---|---|
| **Source** | Pima Indians Diabetes dataset (UCI Machine Learning Repository) |
| **Observations** | n = 768 female patients aged ≥ 21 |
| **Response variable** | Diabetes diagnosis (binary: positive / negative) |
| **Predictors** | Number of pregnancies, plasma glucose concentration, diastolic blood pressure, triceps skin fold thickness, 2-hour serum insulin, BMI, diabetes pedigree function (DPF), age |

---

## Methods / Methoden

- Descriptive analysis and missing value handling (median imputation)
- Complete separation detection (`detectseparation`)
- Binary logistic regression fitted via iteratively reweighted least squares (IRLS)
- Model diagnostics: deviance residuals, Cook's distance, leverage
- Goodness-of-fit: Hosmer-Lemeshow test
- Odds ratio interpretation with 95% confidence intervals
- Classification performance: ROC curve, AUC, sensitivity, specificity, optimal threshold selection

---

## Results / Ergebnisse

- AUC-ROC: **0.787** — model discriminates well between diabetic and non-diabetic patients
- Glucose concentration is the single strongest predictor by a large margin
- BMI and number of pregnancies are the next most influential features
- Blood pressure has near-zero predictive weight in this dataset
- Skin thickness and insulin were excluded due to high missingness (>30%)

---

## Software

**R analysis:**
R 4.5.x · `tidyverse` · `ggplot2` · `patchwork` · `car` · `GGally` · `detectseparation` · `pROC`

**Python / Streamlit app:**
Python 3.12 · `pandas` · `numpy` · `scikit-learn` · `streamlit`

