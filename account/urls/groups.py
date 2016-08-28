# coding: utf-8

from django.conf.urls import url
from account.views import groups

urlpatterns = [
    url(
        r'^$',
        groups.overview,
        name='groups_overview'
    ),
]

