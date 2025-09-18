
import joblib
import pandas as pd
import streamlit as st
# Ensure required packages
for pkg in ["joblib", "pandas", "scikit-learn", "streamlit"]:
    install_if_missing(pkg)

import joblib
import pandas as pd
import streamlit as st
import subprocess
import sys

# Install joblib if missing
try:
    import joblib
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "joblib"])
    import joblib


# Load the model
try:
    model = joblib.load("vl_model.pkl")
except Exception as e:
    st.error(f"❌ Could not load model: {e}")
    st.stop()

st.title("Viral Load Suppression Predictor")

# Example input form
age = st.number_input("Enter Age:", min_value=0, max_value=100, step=1)
cd4 = st.number_input("Enter CD4 Count:", min_value=0, max_value=2000, step=10)

if st.button("Predict"):
    try:
        prediction = model.predict([[age, cd4]])
        result = "Suppressed" if prediction[0] == 1 else "Not Suppressed"
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
