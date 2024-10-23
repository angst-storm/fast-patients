install:
	pip install -r requirements.txt

init: install

ruff:
	ruff format
	ruff check