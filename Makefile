install:
	poetry install

lint:
	poetry run flake8 task_manager

start-dev:
	poetry run python manage.py runserver
