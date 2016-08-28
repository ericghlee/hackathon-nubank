# coding: utf-8

from django.core.validators import EMPTY_VALUES, ValidationError
from django.utils.translation import ugettext_lazy as _
import re


def validate_cpf(value):
    if value in EMPTY_VALUES:
        return ''

    if not is_valid_cpf(value):
        raise ValidationError(_('CPF Inválido'))

    return value


def is_valid_cpf(cpf):
    """Diz se uma string representa um CPF valido ou não.
    A entrada pode ser uma string só com números ou algo no formato
    `XXX.XXX.XXX-XX`. Esse algorítmo é um pouco diferente do que está no site
    da receita federal, mas dá os mesmos resultados. O código foi tirado daqui:
        https://pt.wikipedia.org/wiki/Cadastro_de_Pessoas_Físicas
    """

    def hash_sequence(sequence):
        hash = 0
        for index, value in enumerate(sequence):
            hash += (index + 1) * value
        return (hash % 11) % 10

    only_numbers_re = re.compile(r'[0-9]{11}')
    formatted_cpf_re = re.compile(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}')

    if not (only_numbers_re.match(cpf) or formatted_cpf_re.match(cpf)):
        return False

    # remove traços e pontos do cpf
    cpf = re.sub(r'[-\.]', '', cpf)

    # CPFs com todos os números iguais são inválidos
    invalid_cpfs = [str(number) * 11 for number in range(10)]
    if cpf in invalid_cpfs:
        return False

    cpf = list(map(int, cpf))

    check_digits = [0, 0]
    check_digits[0] = hash_sequence(cpf[:9])
    check_digits[1] = hash_sequence(cpf[1:9] + check_digits[:1])

    return cpf[9:] == check_digits
