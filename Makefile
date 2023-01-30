install:
	poetry install

lint:
	poetry run flake8 task_manager
	
makemessages:
	poetry run django-admin makemessages --ignore="static" --ignore=".env" -l ru
	poetry run django-admin makemessages --ignore="static" --ignore=".env" -l en
	
compilemessages:
	poetry run django-admin compilemessages	

start-dev:
	poetry run python manage.py runserver
