#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import pickle
import numpy as np


# In[6]:


st.title("Iris Classification Demo")


# In[7]:


# Load the saved model
@st.cache_data
def load_model():
    with open("models/trained_model.pkl", "rb") as f:
        model = pickle.load(f)
        return model


# In[8]:


model = load_model()
# Create inputs for features
sepal_length = st.number_input("Sepal length", 0.0, 10.0, 5.1)
sepal_width = st.number_input("Sepal width", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal length", 0.0, 10.0, 1.4)
petal_width = st.number_input("Petal width", 0.0, 10.0, 0.2)

if st.button("Predict"):
    X_sample = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(X_sample)
    st.write(f"Predicted class: {prediction[0]}")

