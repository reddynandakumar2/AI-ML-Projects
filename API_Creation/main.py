from fastapi import FastAPI

app = FastAPI()

@app.get("/student/{id}")
def get_student(id:int):
    return {"student_id": id}