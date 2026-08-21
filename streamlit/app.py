import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

## Load and prepare data
@st.cache_data
def load_and_train():
    cols = [
        "pregnancies", "glucose", "blood_pressure", "skin_thickness",
        "insulin", "bmi", "diabetes_pedigree", "age", "outcome"
    ]
    df = pd.read_csv("diabetes.csv", header=0, names=cols, skiprows=1)

    #replace impossible zeros with NaN
    zero_cols = ["glucose", "blood_pressure", "skin_thickness", "insulin", "bmi"]
    df[zero_cols] = df[zero_cols].replace(0, np.nan)

    #drop high-missingness columns
    df = df.drop(columns=["skin_thickness", "insulin"])

    #median imputation
    for col in ["glucose", "blood_pressure", "bmi"]:
        df[col] = df[col].fillna(df[col].median())

    #train model
    X = df.drop(columns=["outcome"])
    y = df["outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_sc = scaler.fit_transform(X_train)
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train_sc, y_train)

    return model, scaler

model, scaler = load_and_train()

## App layout
st.title("Diabetes Risk Predictor")
st.markdown(
    "Enter patient values below to estimate the probability of diabetes. "
    "Based on the Pima Indians Diabetes Dataset (UCI Machine Learning Repository)."
)

st.header("Patient Input")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.slider("Number of pregnancies", 0, 17, 3)
    glucose = st.slider("Glucose level (mg/dL)", 50, 200, 117)
    blood_pressure = st.slider("Blood pressure (mm Hg)", 20, 130, 72)

with col2:
    bmi = st.slider("BMI", 10.0, 70.0, 32.0, step=0.1)
    diabetes_pedigree = st.slider("Diabetes pedigree function", 0.05, 2.5, 0.47, step=0.01)
    age = st.slider("Age", 18, 90, 33)

## Prediction
input_data = pd.DataFrame([[pregnancies, glucose, blood_pressure, bmi, diabetes_pedigree, age]],
    columns=["pregnancies", "glucose", "blood_pressure", "bmi", "diabetes_pedigree", "age"])

input_scaled = scaler.transform(input_data)
prob = model.predict_proba(input_scaled)[0][1]

st.header("Prediction")

if prob >= 0.5:
    st.error(f"High risk: {prob:.1%} probability of diabetes")
else:
    st.success(f"Low risk: {prob:.1%} probability of diabetes")

st.progress(float(prob))

## Feature importance
st.header("Most influential factors")
st.markdown(
    "Glucose level and BMI are the strongest predictors in this model. "
    "Blood pressure has almost no predictive weight."
)
