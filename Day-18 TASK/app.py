import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import pickle
model_path = os.path.join(os.path.dirname(__file__), "churn_model.pkl")
model = pickle.load(open(model_path, "rb"))
def main():
    st.title("Customer Churn Prediction")
    st.write("Enter the most important customer details to predict churn.")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=0)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=0.0)
    total_charges = st.number_input("Total Charges", min_value=0.0, value=0.0)

    if st.button("Predict Churn"):
        input_data = pd.DataFrame({
            'gender': [gender],
            'SeniorCitizen': [1 if senior_citizen == "Yes" else 0],
            'tenure': [tenure],
            'Contract': [contract],
            'PaperlessBilling': [1 if paperless_billing == "Yes" else 0],
            'PaymentMethod': [payment_method],
            'MonthlyCharges': [monthly_charges],
            'TotalCharges': [total_charges],
            'Partner': [0],
            'Dependents': [0],
            'PhoneService': [0],
            'MultipleLines': ['No'],
            'InternetService': ['No'],
            'OnlineSecurity': ['No'],
            'OnlineBackup': ['No'],
            'DeviceProtection': ['No'],
            'TechSupport': ['No'],
            'StreamingTV': ['No'],
            'StreamingMovies': ['No']
        })
        input_data = pd.get_dummies(input_data)
        input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)
        prediction = model.predict(input_data)
        if prediction[0] == 1:
            st.error("The customer is likely to churn.")
        else:
            st.success("The customer is unlikely to churn.")
if __name__ == "__main__":
    main()
