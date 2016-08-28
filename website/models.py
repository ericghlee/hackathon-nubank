from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from website.utils.validators import validate_cpf


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, cpf, password=None):
        if not email:
            msg = 'Entre com um endereço de email'
            raise ValueError(msg)

        if not full_name:
            msg = 'Entre com o nome completo do usuário'
            raise ValueError(msg)

        user = self.model(
            email=UserManager.normalize_email(email),
            full_name=full_name,
            first_name=full_name.split(None, 1)[:1],
            last_name=full_name.split(None, 1)[1:],
            cpf=cpf
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, cpf, password=None):
        user = self.create_user(email, full_name, cpf, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        'Email',
        max_length=254,
        unique=True,
        db_index=True
    )

    full_name = models.CharField(
        'Nome completo',
        max_length=255
    )
    cpf = models.CharField(
        'CPF',
        max_length=11,
        validators=[
            validate_cpf
        ],
    )
    phone = models.CharField(
        'Telefone',
        max_length=16,
        blank=True,
        null=True
    )
    # campos que o django-cms exige
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'usuário'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email