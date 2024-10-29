from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import itertools

ids = itertools.count()
NOT_FOUND_ERROR = HTTPException(status_code=404, detail="Patient not found")


class PatientIn(BaseModel):
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


patients: list[Patient] = []


def find_patient(patient_id: int) -> tuple[int, Patient] | None:
    return next(((i, p) for i, p in enumerate(patients) if p.id == patient_id), None)


app = FastAPI()


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/patients")
def patients_list() -> list[Patient]:
    return patients


@app.post("/patients")
def patient_create(data: PatientIn) -> Patient:
    patient = Patient(**data.model_dump(), id=next(ids))
    patients.append(patient)
    return patient


@app.get("/patients/{patient_id}", responses={404: {}})
def patient_select(patient_id: int) -> Patient:
    (_, patient) = find_patient(patient_id)
    if patient is None:
        raise NOT_FOUND_ERROR
    return patient


@app.put("/patients/{patient_id}", responses={404: {}})
def patient_update(patient_id: int, data: PatientIn) -> Patient:
    (index, _) = find_patient(patient_id)
    if index is None:
        raise NOT_FOUND_ERROR
    patient = patients.pop(index)
    new_patient = patient.model_copy(update=data.model_dump())
    patients.append(new_patient)
    return new_patient


@app.delete("/patients/{patient_id}", responses={404: {}})
def patient_delete(patient_id: int) -> Patient:
    (index, _) = find_patient(patient_id)
    if index is None:
        raise NOT_FOUND_ERROR
    patient = patients.pop(index)
    return patient
