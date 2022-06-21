release: python manage.py migrate --no-input


web: gunicorn blog.wsgi:application --log-file -