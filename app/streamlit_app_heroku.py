import streamlit as st
import requests

st.title("Model Inference via Heroku API")

# Input for features
features = st.text_input("Features (comma-separated):", "5.1,3.5,1.4,0.2")

# Predict button
if st.button("Predict"):
    try:
        # Prepare data: Convert input string to list of floats
        data = [list(map(float, (feature.strip() for feature in features.split(","))))]
        # Heroku API URL
        api_url = "https://testingdeployementiris-32f29fb390ef.herokuapp.com/predict"

        # Make POST request to the API
        response = requests.post(api_url, json=data)

        # Check if the request was successful
        if response.status_code == 200:
            predictions = response.json().get("predictions", [])
            st.success(f"Predictions: {predictions}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")