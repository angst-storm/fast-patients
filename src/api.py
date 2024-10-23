from fastapi import FastAPI, HTTPException
from .db import Patient
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.get("/", include_in_schema=False)
def index()-> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/patients")
def patients_list() -> list[Patient]:
    return Patient.all()


@app.get("/patients/{patient_id}", responses={404: {}})
def patients_select(patient_id: int) -> Patient:
    result = Patient.select(patient_id)
    if not result:
        raise HTTPException(status_code=404, detail="Patient not found")
    return result
