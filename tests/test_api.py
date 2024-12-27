#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pytest
from fastapi.testclient import TestClient
import sys
# sys.path.append('C:/Users/oquach/Documents/OpenClassRoom/Iris/app')
from app.main import app


# In[27]:


client = TestClient(app)


# In[30]:


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert "API is running" in res.json()["message"]

def test_predict():
    #payload = {"data": [[5.1, 3.5, 1.4, 0.2]]}
    payload = [[5.1, 3.5, 1.4, 0.2]]
    res = client.post("/predict", json=payload)
    assert res.status_code == 200
    assert "predictions" in res.json()

