from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("resume_model.pkl")
print(type(model))
print(model)

class ResumeRequest(BaseModel):

    resume_text: str
    Experience: int
    salary_Expectation: int
    Projects: int
    AI_Score: int

@app.get("/")
def home():
    return {
        "message":"API Running"
    }

@app.post("/predict")
def predict(data: ResumeRequest):

    input_df = pd.DataFrame({

        "Text_cols":[data.resume_text],

        "Experience (Years)":[data.Experience],

        "Salary Expectation ($)":[data.salary_Expectation],

        "Projects Count":[data.Projects],

        "AI Score (0-100)":[data.AI_Score]

    })

    prediction = model.predict(input_df)[0]

    decision = (
        "Selected"
        if prediction == 0
        else "Rejected"
    )

    return {

        "Recruiter_Decision": decision

    }