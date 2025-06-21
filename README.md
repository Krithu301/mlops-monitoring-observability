# 🚀 MLOps Monitoring & Observability Project

This project implements complete monitoring and observability for a machine learning system using key tools like Prometheus, Grafana, SHAP, Evidently, MLflow, and Flask.

---

## 📌 Features Implemented

- 📊 Model Monitoring with Prometheus & Grafana
- 📉 Data Drift Detection using Evidently AI
- 🧠 Model Explainability using SHAP
- 🧪 A/B Testing Simulation with Flask
- 📈 Model Tracking using MLflow

---

## 🧰 Technologies Used

- Python
- Flask
- Prometheus
- Grafana
- SHAP
- MLflow
- Evidently
- scikit-learn

---

## 📁 Project Structure

mlops-monitoring/ ├── flask_app.py              # Prometheus metrics endpoint ├── prometheus.yml            # Prometheus scrape configuration ├── ab_test_flask.py          # A/B test simulation ├── mlflow_tracking.py        # Logs model to MLflow ├── data_drift_report.html    # HTML report from Evidently ├── shap_plot.png             # SHAP summary plot image ├── requirements.txt          # Python dependencies └── README.md                 # Project documentation

---

## 🔧 Setup Instructions

1. Clone the Repository

git clone https://github.com/yourusername/mlops-monitoring.git
cd mlops-monitoring

2. Install Dependencies

pip install -r requirements.txt

---

🚀 Usage

▶ Run Prometheus Metrics Flask App

python flask_app.py

Visit: http://localhost:8000/metrics


---

▶ Start Prometheus

prometheus --config.file=prometheus.yml


---

▶ Open Grafana

Navigate to: http://localhost:3000
Login and configure Prometheus as a data source.


---

▶ SHAP Explainability

Run SHAP analysis:

python shap_explain.py

This shows feature importance for model predictions.


---

▶ A/B Testing Simulation

python ab_test_flask.py

Visit: http://localhost:8001/predict
Each refresh returns Model A or Model B randomly.


---

▶ MLflow Tracking

Run:

python mlflow_tracking.py

Then start MLflow UI:

python -m mlflow ui

Visit: http://localhost:5000 to view model logs and metrics.


---

📸 Sample Screenshots

1.![Screenshot (30)](https://github.com/user-attachments/assets/3659a5e4-aad7-4a3c-8959-ce25b51621dd)
2.![Screenshot (32)](https://github.com/user-attachments/assets/e13ccdff-97c8-4265-bf43-edf066dfdfd1)
3.![Screenshot (35)](https://github.com/user-attachments/assets/5719de08-89a2-4274-b9f1-e67ed37811d1)
4.![Screenshot (36)](https://github.com/user-attachments/assets/374858c4-1c7a-4c2a-b7be-7af6bcbe0a02)
5.![Screenshot (33)](https://github.com/user-attachments/assets/8aea7f17-3d65-4b08-8652-0eb31605e463)
6.![Screenshot (34)](https://github.com/user-attachments/assets/97358128-5931-4a66-bc02-dace1926a1e4)
