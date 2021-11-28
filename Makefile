style:
	poetry run black demapi tests && poetry run isort demapi tests

install:
	poetry install --no-dev

install-all:
	poetry install -E all && poetry run pre-commit install

install-check:
	poetry install -E check && poetry run pre-commit install

install-test:
	poetry install -E test && poetry run pre-commit install

install-style:
	poetry install -E style && poetry run pre-commit install

test-ci:
	poetry run coverage run --source=demapi -m pytest tests

test:
	poetry run pytest tests --cov=demapi --cov-report=html

serve-cov:
	poetry run python -m http.server -d htmlcov -b 127.0.0.1

check:
	poetry run mypy --strict
