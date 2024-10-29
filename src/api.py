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
def patients_create(data: PatientCreate) -> Patient:
    patient = Patient(**data.model_dump(), id=ids.__next__())
    patients.append(patient)
    return patient


@app.get("/patients/{patient_id}", responses={404: {}})
def patients_select(patient_id: int) -> Patient:
    result = [p for p in patients if p.id == patient_id]
    if len(result) == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return result[0]
