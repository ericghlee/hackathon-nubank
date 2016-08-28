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
        r'^participate/(\d+)$',
        groups.participate,
        name='groups_participate'
    ),
    url(
        r'^leave/(\d+)$',
        groups.leave,
        name='groups_leave'
    ),
    url(
        r'^add/$',
        groups.add,
        name='groups_add'
    ),
]

