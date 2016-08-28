# coding: utf-8

from django.conf.urls import url
from account.views import cards

urlpatterns = [
    url(
        r'^$',
        cards.cards,
        name='card_index'
    ),
]
