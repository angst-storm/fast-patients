from .db import db

if __name__ == "__main__":
    db.drop_tables()
    db.insert({"id": 1, "name": "Sergei Kiprin"})
    db.insert({"id": 2, "name": "John Who"})
