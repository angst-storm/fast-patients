install:
	pip install -r requirements.txt

run:
	fastapi dev src/api.py

ruff:
	ruff format
	ruff check