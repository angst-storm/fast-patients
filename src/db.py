from pydantic import BaseModel
from tinydb import TinyDB, Query

db = TinyDB("db.json")
PatientQ = Query()


class Patient(BaseModel):
    id: int
    name: str

    @staticmethod
    def all():
        return [Patient(**p) for p in db.all()]

    @staticmethod
    def select(id: int):
        result = db.get(PatientQ.id == id)
        return Patient(**result) if result else None
