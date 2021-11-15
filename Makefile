.SILENT: fmt check lint

fmt:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		pydantic_secret_decimal*.py
	isort --profile black .
	black .

check:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		pydantic_secret_decimal*.py
	isort --profile black -c .
	black --check .

lint:
	mypy pydantic_secret_decimal*.py
	flake8 .

test:
	pytest -x --cov=core --cov=pydantic_secret_decimal --cov-fail-under=90
