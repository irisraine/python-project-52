install:
	poetry install

lint:
	poetry run flake8 task_manager
	
makemigrations:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate

makemessages:
	poetry run django-admin makemessages --ignore="static" --ignore=".env" -l ru
	poetry run django-admin makemessages --ignore="static" --ignore=".env" -l en
	
compilemessages:
	poetry run django-admin compilemessages
	
start:
	poetry run gunicorn --workers=5 task_manager.wsgi	

start-dev:
	poetry run python manage.py runserver
	
coverage:
	poetry run coverage run --source='.' manage.py test
	poetry run coverage xml
