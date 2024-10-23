from fastapi import FastAPI
from .db import Patient


app = FastAPI()


@app.get("/patients")
def read_root():
    return [Patient(**{"id": 1, "name": "test"})]


@app.get("/patients/{patient_id}")
def read_item(patient_id: int):
    return Patient(**{"id": patient_id, "name": "test"})
