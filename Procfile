release: python manage.py migrate --no-input


web: gunicorn api.wsgi:application --log-file -