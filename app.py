import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Model/model.pkl")

# Set page title
st.title("💰 Gold Price Prediction App")

st.markdown("""
Enter the financial indicators below to predict the price of gold (GLD):
""")

# Input fields
spx = st.number_input("SPX (S&P 500 Index)", min_value=0.0, format="%.2f")
uso = st.number_input("USO (Crude Oil ETF)", min_value=0.0, format="%.2f")
slv = st.number_input("SLV (Silver Price)", min_value=0.0, format="%.2f")
eur_usd = st.number_input("EUR/USD Exchange Rate", min_value=0.0, format="%.4f")

# Prediction
if st.button("Predict"):
    features = np.array([[spx, uso, slv, eur_usd]])
    prediction = model.predict(features)[0]
    st.success(f"📈 Predicted Gold Price: ${round(prediction, 2)}")
