style:
	poetry run black demapi tests && poetry run isort demapi tests

install:
	poetry install --no-dev

install-dev:
	poetry install && poetry run pre-commit install

test-ci:
	poetry run coverage run --source=demapi -m pytest tests
