# ML Engineering Pipeline 🚀

An end-to-end machine learning system with API, database logging, Dockerization, and cloud deployment.

---

## 📌 Overview

This project demonstrates a **production-style ML pipeline**, including:

* Data ingestion from CSV into a database
* Model training and inference
* REST API built with FastAPI
* Logging predictions into a database
* Dockerized application for reproducibility
* Cloud deployment using Render

The system allows users to send requests to an API and receive predictions, while storing all interactions for monitoring and analysis.

---

## 🏗️ Architecture

```text
User → FastAPI → Model → Database → Logs
```

* **FastAPI** handles API requests
* **Model** is loaded from disk for predictions
* **SQLite database** stores inference logs
* **Docker** ensures consistent environment
* **Render** hosts the live API

---

## 🌐 Live Demo

👉 https://ml-engineering-template-1.onrender.com/docs

You can interact with the API directly via Swagger UI.

---

## ⚙️ Run Locally

```bash
git clone https://github.com/your-username/ml-engineering-template.git
cd ml-engineering-template

pip install -r requirements.txt

uvicorn src.app.api:app --reload
```

Then open:

👉 http://127.0.0.1:8000/docs

---

## 🐳 Run with Docker

```bash
docker build -t ml-api .
docker run -p 8000:8000 ml-api
```

Then open:

👉 http://localhost:8000/docs

---

## 📡 API Endpoints

### 🔹 Predict

**POST /predict**

```json
{
  "feature": 101
}
```

Returns:

```json
{
  "prediction": 1
}
```

---

### 🔹 Logs

**GET /logs**

Returns stored prediction logs from the database.

---

## 📁 Project Structure

```text
ml-engineering-template/
│
├── src/app/           # Core application (API, model, DB)
├── scripts/           # Data ingestion & utilities
├── models/            # Trained model files
├── database/          # SQL schema
├── tests/             # Unit tests
├── Dockerfile         # Container setup
├── requirements.txt   # Dependencies
└── README.md
```

---

## 🧠 Features

* End-to-end ML pipeline
* FastAPI-based REST service
* Structured logging of predictions
* Dockerized deployment
* Cloud-hosted API (Render)

---

## 🚀 Future Improvements

* Replace SQLite with PostgreSQL
* Add model versioning
* Add monitoring & metrics (Prometheus)
* Improve test coverage
* Add authentication

---

## 💼 Resume Highlight

This project demonstrates:

* Building production-ready ML systems
* API development with FastAPI
* Containerization with Docker
* Cloud deployment (Render)
* Data engineering + ML integration

---

## 👤 Author

Mina Nourhashemi
