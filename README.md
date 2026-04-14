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

🖥️ Project Demo
Dashboard

<img width="640" height="480" alt="Figure_p3-1" src="https://github.com/user-attachments/assets/12c0c4ad-eb5d-439e-bf98-569c2bb9dbae" />

## Normal Prediction

<img width="1920" height="1080" alt="Screenshot (10)" src="https://github.com/user-attachments/assets/b3bf2c22-bcc4-40f7-a561-c420ca79beb4" />

## Threat Detection

<img width="640" height="480" alt="confusion_matrix" src="https://github.com/user-attachments/assets/9a76bf88-0165-422f-8c25-fca565d632fb" />

## Confusion Matrix

📌 Future Improvements
Use real datasets (CICIDS, NSL-KDD)
Add attack type classification
Deploy on cloud (AWS / GCP)
Real-time network traffic monitoring
🎯 Learning Outcomes
Machine Learning pipeline development
Data preprocessing & feature engineering
Model evaluation techniques
Building interactive dashboards with Streamlit

👨‍💻 Author
Challa Kishore

