install:
	pip install -r requirements.txt

run:
	fastapi dev src/api.py

export_doc:
	python -m src.export_doc

ruff:
	ruff format
	ruff check