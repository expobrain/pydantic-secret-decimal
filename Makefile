.SILENT: lint

lint:
	mypy pydantic_secret_decimal*.py
	flake8 .

test:
	pytest -x --cov=core --cov=pydantic_secret_decimal --cov-fail-under=90
