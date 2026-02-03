from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from typing import List

# Create FastAPI app
app = FastAPI(title="Milestone 1 - Model Serving")
@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}


# Load model ONCE at startup (VERY IMPORTANT)
model = joblib.load("model.pkl")

# Request schema
class PredictRequest(BaseModel):
    features: List[float]

# Response schema
class PredictResponse(BaseModel):
    prediction: float
    model_version: str

# Prediction endpoint
@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    prediction = model.predict([request.features])[0]
    return PredictResponse(
        prediction=float(prediction),
        model_version="v1"
    )
