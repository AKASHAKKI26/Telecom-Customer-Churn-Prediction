# Telecom Customer Churn Prediction

This project predicts whether a customer is likely to churn using Machine Learning and Streamlit.

## Features
- Customer churn prediction
- Streamlit web application
- Trained ML model using Scikit-learn
- Simple and user-friendly interface

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

## Project Structure

```bash
├── app.py
├── churn_model.pkl
├── prediction.ipynb
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
cd customer-churn-prediction
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app

```bash
streamlit run app.py
```

## Input Features
- Gender
- Senior Citizen
- Tenure
- Contract
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges

## Output
- Customer likely to churn
- Customer unlikely to churn

## Model
The trained model is stored in:
- `churn_model.pkl`

## Author
Akash
