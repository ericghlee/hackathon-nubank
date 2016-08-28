from django import forms
from account.models import CreditCard, Group


class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['owner']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']