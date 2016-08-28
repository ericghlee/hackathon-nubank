from django.core.validators import RegexValidator
from django.db import models
from website.models import User

# Create your models here.
class CreditCard(models.Model):

    number = models.CharField(
        'Número do cartão',
        max_length=16,
        validators=[
            RegexValidator(regex='\d{16}')
        ])

    full_name = models.CharField(
        'Nome completo',
        max_length=255
    )

    expiration_date = models.DateField('Data de validade')

    verification_code = models.SmallIntegerField('Código de segurança')

    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_credit_card_number(self):
        return "**** **** **** " + self.number[-4:]

    def get_owner(self):
        return self.owner

