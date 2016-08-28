# coding: utf-8

from django.conf.urls import url, include

urlpatterns = [
    url(r'^grupos/', include('account.urls.groups')),
    url(r'^cards/', include('account.urls.cards')),
    url('^', include('django.contrib.auth.urls')),
]

