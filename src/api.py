from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    med_record_number: int


patients: dict[int, Patient] = {}
app = FastAPI()


@app.get("/", include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.get("/patients")
def patients_list() -> list[Patient]:
    return list(patients.values())


@app.get("/patients/{patient_id}", responses={404: {}})
def patients_select(patient_id: int) -> Patient:
    result = patients.get(patient_id)
    if not result:
        raise HTTPException(status_code=404, detail="Patient not found")
    return result
