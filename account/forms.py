from django import forms
from account.models import CreditCard, Group, Invitation


class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['owner']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class CardSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs['user']
        kwargs.__delitem__('user');
        super(CardSelectForm, self).__init__(*args, **kwargs)

        self.fields['card'] = forms.ChoiceField(
            label="Usuário", 
            choices=[(o.id, str(o)) for o in CreditCard.objects.filter(owner=user)]
        )


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['user']
