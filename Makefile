style:
	poetry run black demapi tests && poetry run isort demapi tests

install:
	poetry install --no-dev

install-dev:
	poetry install && poetry run pre-commit install

tests:
	poetry run pytest tests --cov=demapi --cov-report=html
