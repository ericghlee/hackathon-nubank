# coding: utf-8

from django.conf.urls import url, include

urlpatterns = [
    url(r'^grupos/', include('account.urls.groups')),
    url('^', include('django.contrib.auth.urls')),
]
