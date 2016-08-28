from django.shortcuts import render, redirect, get_object_or_404
from account.models import CreditCard
from django.contrib.auth.decorators import login_required
from account.forms import CreditCardForm


@login_required
def cards(request):
    cards = CreditCard.objects.filter(owner=request.user)

    return render(request,'account/cards/card.html', {"cards" : cards})


@login_required
def cards_add(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect('card_index')
    else:
        form = CreditCardForm()

    return render(request,'account/cards/card_add.html', {"form": form})


@login_required
def cards_remove(request, pk):
    card = get_object_or_404(CreditCard, pk=pk)
    card.delete()
    return redirect('card_index')