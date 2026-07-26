# Thema 4 — Logistic Regression for Diabetes Prediction
**Logistische Regression zur Vorhersage von Diabetes**

**Technische Universität Dortmund | Department of Statistics | SoSe 2026**
Supervised by Prof. Dr. Katja Ickstadt, JProf. Dr. Nils Weitzel, Dr. Zeyu Ding
Author: Ganeisraaj Kathiravan | Group partner: Jakub Marczat

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

├── report.pdf        # English-language report
├── analysis.R        # R script
└── data/
    └── pima.csv
```

---

## Software

R 4.5.x · `tidyverse` · `ggplot2` · `patchwork` · `car` · `GGally` · `detectseparation` · `pROC`
