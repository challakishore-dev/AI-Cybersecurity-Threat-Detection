# 🔐 AI-Powered Cybersecurity Threat Detection

## 📌 Overview
This project is a machine learning-based cybersecurity system that detects suspicious or malicious network activity.

It analyzes network features such as login attempts, traffic patterns, and request frequency to classify behavior as **Normal** or **Threat**.

---

## 🚀 Features
- Machine Learning model (Random Forest)
- Real-time prediction using Streamlit dashboard
- Threat detection based on behavioral patterns
- Confusion matrix visualization
- Clean and modular project structure

---

## 🧠 Problem Statement
Traditional security systems rely on static rules and fail to detect new or unknown attacks.

This project uses AI to:
- Learn patterns from data
- Detect anomalies dynamically
- Identify potential cyber threats

---

## 🏗️ Project Architecture
Data → Preprocessing → Model Training → Prediction → Dashboard (Streamlit)


---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## 📂 Project Structure


AI-Cybersecurity-Threat-Detection/
│
├── data/ # Dataset
├── models/ # Trained model
├── images/ # Graphs & screenshots
├── src/ # Source code
├── main.py # Training script
├── app.py # Streamlit UI
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

```bash
pip install -r requirements.txt
▶️ Run the Project
Step 1: Train model
python main.py
Step 2: Run dashboard
python -m streamlit run app.py

📊 Results

Model Accuracy: ~100% (synthetic dataset)
Evaluation Metrics: Precision, Recall, F1-score
Confusion Matrix generated
