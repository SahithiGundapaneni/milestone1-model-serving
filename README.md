# Milestone 1 – Model Serving with FastAPI

This project implements **Milestone 1: Model Serving** for the MLOps course.  
A trained machine learning model is served through a REST API using **FastAPI** and **Docker**, and tested locally.

---

## 📌 Project Overview

- A machine learning model is trained locally
- The trained model is saved as a serialized artifact (`model.pkl`)
- A FastAPI application loads the model at startup
- A `/predict` endpoint exposes the model for inference
- The application is containerized using Docker
- The service is tested locally using Swagger UI

---

## 📁 Project Structure




