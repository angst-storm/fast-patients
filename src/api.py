from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import itertools


class PatientCreate(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    med_record_number: int


class Patient(BaseModel):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    med_record_number: int


ids = itertools.count()
patients: list[Patient] = []
app = FastAPI()


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/patients")
def patients_list() -> list[Patient]:
    return patients


@app.post("/patients")
def patient_create(data: PatientCreate) -> Patient:
    patient = Patient(**data.model_dump(), id=next(ids))
    patients.append(patient)
    return patient


@app.delete("/patients/{patient_id}")
def patient_delete(patient_id: int) -> Patient:
    index = next((i for i, p in enumerate(patients) if p.id == patient_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    patient = patients.pop(index)
    return patient


@app.get("/patients/{patient_id}", responses={404: {}})
def patient_select(patient_id: int) -> Patient:
    patient = next((p for p in patients if p.id == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient
