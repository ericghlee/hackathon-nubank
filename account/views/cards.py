from django.shortcuts import render
from account.models import CreditCard
from django.contrib.auth.decorators import login_required

@login_required
def cards(request):
	cards = CreditCard.objects.filter(owner=request.user)

	return render(request,'account/cards/card.html', {"cards" : cards})