from pydantic import BaseModel
from tinydb import TinyDB, Query

db = TinyDB("db.json")
PatientQ = Query()


class Patient(BaseModel):
    id: int
    name: str

    @staticmethod
    def all():
        return db.all()

    @staticmethod
    def select(id: int):
        return db.search(PatientQ.id == id)
