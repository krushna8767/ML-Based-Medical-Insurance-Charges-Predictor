import streamlit as st
import pickle
import numpy as np

# Load the trained model
# Make sure your 'best_model.pkl' file is in the same directory
try:
    with open("best_model.pkl", "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Error: 'best_model.pkl' not found. Please ensure the model file is in the same directory.")
    model = None  # Set model to None to prevent errors later

# --- LEFT SIDEBAR (NEW ADDITION) ---
st.sidebar.title("👨‍💻 Developer Info")
st.sidebar.markdown("""
### Krushna Shinde
""")

# Replace the placeholders below with your actual links
st.sidebar.markdown("""
**GitHub:** https://github.com/krushna8767
""")
st.sidebar.markdown("---")
# --- END OF SIDEBAR ---

st.title("🏥 Medical Insurance Charges Predictor")

st.write("""
This app predicts **Medical Insurance Charges** based on:
- Age  
- BMI  
- Smoking Status
""")

# Collect user input
age = st.number_input("Enter Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=60.0, value=25.0)
smoker = st.selectbox("Are you a smoker?", ["No", "Yes"])

# Encode smoker variable (same as in training)
smoker_yes = 1 if smoker == "Yes" else 0

# Prepare input for prediction
input_data = np.array([[age, bmi, smoker_yes]])

# Predict charges
if st.button("Predict Charges"):
    if model:
        prediction = model.predict(input_data)
        st.success(f"💰 Estimated Medical Charges: **${prediction[0]:,.2f}**")
    else:
        st.warning("Prediction cannot be made because the model file was not loaded.")
