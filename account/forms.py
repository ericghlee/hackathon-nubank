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


class CardSelectForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(CardSelectForm, self).__init__(*args, **kwargs)
        self.fields['card'] = forms.ChoiceField(
            choices=[(o.id, str(o)) for o in CreditCard.objects.filter(owner=user)]
        )