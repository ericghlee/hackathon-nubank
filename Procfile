web: rm db.sqlite3
web: python manage.py migrate
web: python default-user.py
web: python manage.py runserver 0.0.0.0:$PORT --noreload
