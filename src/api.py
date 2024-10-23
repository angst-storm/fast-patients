from fastapi import FastAPI, HTTPException
from .db import Patient


app = FastAPI()


@app.get("/patients")
def patient_list():
    return Patient.all()


@app.get("/patients/{patient_id}")
def patient_select(patient_id: int):
    result = Patient.select(patient_id)
    if len(result) == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return result
