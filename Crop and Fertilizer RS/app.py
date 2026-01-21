import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("crop_model.pkl", "rb"))

# Crop mapping (reverse mapping for prediction)
crop_dict = {
    0: 'rice',
    1: 'maize',
    2: 'chickpea',
    3: 'kidneybeans',
    4: 'mungbean',
    5: 'blackgram',
    6: 'lentil',
    7: 'pomegranate',
    8: 'banana',
    9: 'mango',
    10: 'grapes',
    11: 'watermelon',
    12: 'muskmelon',
    13: 'apple',
    14: 'orange',
    15: 'papaya',
    16: 'coconut',
    17: 'cotton',
    18: 'jute',
    19: 'coffee'
}

# Page config
st.set_page_config(page_title="Crop Recommendation System", page_icon="🌱")

st.title("🌾 Crop Recommendation System")
st.write("Enter soil and climate details to get the best crop recommendation")

# User inputs
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("Soil pH")
rainfall = st.number_input("Rainfall (mm)")

# Prediction
if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    crop_name = crop_dict[prediction]

    st.success(f"🌱 Recommended Crop: **{crop_name.upper()}**")
