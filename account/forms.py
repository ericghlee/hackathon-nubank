from django import forms
from account.models import CreditCard


class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['owner']