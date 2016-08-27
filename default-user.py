# coding: utf-8
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "hackathon.settings"  # noqa
import django
django.setup()  # noqa

from website.models import User

User.objects.create_superuser('admin@admin.net', 'Administrador Fodão', '12345678909', 'senha')