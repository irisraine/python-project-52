web: gunicorn task_manager.wsgi --log-file -
release: python manage.py collectstatic && python manage.py migrate
