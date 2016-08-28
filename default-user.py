# coding: utf-8
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackathon.settings.dev")
import django
django.setup()  # noqa

from website.models import User

User.objects.create_superuser('admin1', 'admin1@admin.net', 'Andre Missaglia', '12345678909', 'senha')
User.objects.create_superuser('admin2', 'admin2@admin.net', 'Eric Lee', '12345678910', 'senha')
User.objects.create_superuser('admin3', 'admin3@admin.net', 'Germano Neuenfeld', '12345678911', 'senha')
User.objects.create_superuser('admin4', 'admin4@admin.net', 'Jordana Faria', '12345678912', 'senha')
User.objects.create_superuser('admin5', 'admin5@admin.net', 'Victor Raposo', '12345678913', 'senha')
