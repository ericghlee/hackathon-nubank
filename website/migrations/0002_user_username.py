# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='admin', max_length=255, verbose_name='Username'),
            preserve_default=False,
        ),
    ]