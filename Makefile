install:
	pip install -r requirements.txt

reset-db:
	python -m src.reset_db

init: install reset-db

run:
	fastapi dev src/api.py

ruff:
	ruff format
	ruff check