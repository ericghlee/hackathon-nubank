# coding: utf-8

from django.conf.urls import url
from account.views import groups

urlpatterns = [
    url(
        r'^$',
        groups.overview,
        name='groups_overview'
    ),
    url(
        r'^detailed/(\d+)$',
        groups.detailedview,
        name='groups_detailed'
    ),
    url(
        r'^add/$',
        groups.add,
        name='groups_add'
    ),
]

