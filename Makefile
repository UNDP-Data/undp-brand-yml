install:
	poetry install --with dev
lint:
	pylint undp_brand_yml
format:
	isort . --profile black --multi-line 3 && black .
test:
	python -m pytest tests
