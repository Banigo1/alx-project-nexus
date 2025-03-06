release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn poll_system.wsgi:application