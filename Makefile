install:
	pip install -r requirements.txt

init: install

run:
	fastapi dev src/api.py

ruff:
	ruff format
	ruff check