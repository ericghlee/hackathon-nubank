# coding: utf-8

from django.conf.urls import url
from account.views import cards

urlpatterns = [
    url(
        r'^$',
        cards.cards,
        name='card_index'
    ),
    url(
        r'^add/$',
        cards.cards_add,
        name='card_add'
    ),
    url(
        r'^delete/(\d+)$',
        cards.cards_remove,
        name='card_remove'
    ),
]
