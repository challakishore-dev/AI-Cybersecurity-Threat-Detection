
import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="Cyber Threat Detection PRO", layout="wide")

st.title("🔐 AI Cybersecurity Threat Detection (PRO)")

model = joblib.load("models/model.pkl")

col1,col2 = st.columns(2)

with col1:
    duration = st.slider("Duration",1,100,10)
    src_bytes = st.slider("Source Bytes",1,5000,1000)
    dst_bytes = st.slider("Destination Bytes",1,5000,1000)

with col2:
    failed_logins = st.slider("Failed Logins",0,10,2)
    request_rate = st.slider("Request Rate",1,500,100)

if st.button("🚀 Predict"):
    data = np.array([[duration,src_bytes,dst_bytes,failed_logins,request_rate]])
    pred = model.predict(data)
    prob = model.predict_proba(data)[0][1]

    if pred[0]==1:
        st.error(f"🚨 Threat Detected (Risk: {prob:.2f})")
    else:
        st.success(f"✅ Normal Traffic (Risk: {prob:.2f})")

st.markdown("---")
st.subheader("📊 Project Info")
st.write("Model: Random Forest | Dataset: Simulated Cyber Traffic")
