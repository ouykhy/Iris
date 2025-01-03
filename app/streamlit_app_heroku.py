import streamlit as st
import requests

st.title("Model Inference via Heroku API")

features = st.text_input("Features (comma-separated):", "5.1,3.5,1.4,0.2")

api_url = "https://testingdeployementiris-32f29fb390ef.herokuapp.com/"

if st.button("Predict"):
    try:
        feature_list = list(map(float, (feature.strip() for feature in features.split(","))))
        data = {"features": feature_list}

        # Try POST first
        response = requests.post(api_url, json=data, headers={"Content-Type": "application/json"})

        if response.status_code == 200:
            predictions = response.json().get("predictions", [])
            st.success(f"Predictions: {predictions}")
        elif response.status_code == 405 or response.status_code == 404:
            # Fallback to GET if POST fails
            response = requests.get(api_url, params={"features": features})
            if response.status_code == 200:
                predictions = response.json().get("predictions", [])
                st.success(f"Predictions: {predictions}")
            else:
                st.error(f"GET request failed with status {response.status_code}: {response.text}")
        else:
            st.error(f"POST request failed with status {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
