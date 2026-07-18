from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load model once when server starts
model = joblib.load("salary_model.pkl")


# Input Schema
class Employee(BaseModel):
    experience: float


@app.get("/")
def home():
    return {"message": "Salary Prediction API Running"}


@app.post("/predict")
def predict(data: Employee):

    df = pd.DataFrame(
        [[data.experience]],
        columns=["experience"]
    )

    prediction = model.predict(df)

    return {
        "experience": data.experience,
        "predicted_salary": round(float(prediction[0]), 2)
    }