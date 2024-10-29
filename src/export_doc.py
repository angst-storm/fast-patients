from .api import app
import json

if __name__ == "__main__":
    with open("docs.json", "w") as docs:
        docs.write(json.dumps(app.openapi()))
