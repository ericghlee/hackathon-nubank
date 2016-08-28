from django.core.validators import RegexValidator
from django.db import models
from website.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


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

    expiration_date_month = models.SmallIntegerField(
        'Mês de Vencimento',
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ]
    )
    expiration_date_year = models.SmallIntegerField(
        'Ano de Vencimento',
        validators=[
            MaxValueValidator(99),
            MinValueValidator(0)
        ]
    )

    verification_code = models.SmallIntegerField('Código de segurança')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_credit_card_number(self):
        return "**** **** **** " + self.number[-4:]

    def get_owner(self):
        return self.owner

    def __str__(self):
        return self.get_credit_card_number()


class Group(models.Model):

        name = models.CharField(
            'Nome do Grupo', 
            max_length=255
            )

        cards = models.ManyToManyField(
            CreditCard,
            blank=True,
        )

        def get_name(self):
            return self.name

        def get_users(self):
            return self.get_usr_set.all()

        def users(self):
            return User.objects.filter(creditcard__group=self)


class VirtualCard(models.Model):

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

    owner = models.ForeignKey(Group, on_delete=models.CASCADE)

    def get_credit_card_number(self):
        return self.number


class Invitation(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)