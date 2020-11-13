from django.db import models
from django.utils.translation import gettext as _


class Person(models.Model):
    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    cpf = models.CharField(verbose_name=_("CPF"), max_length=11)

    name = models.CharField(verbose_name=_("Nome"), max_length=255)

    social_name = models.CharField(verbose_name=_("Nome Social"), max_length=255)

    subscription_status = models.CharField(
        verbose_name=_("Situação Cadastral"),
        max_length=255
    )

    stranger_resident = models.CharField(
        verbose_name=_("Residente no Exterior"),
        max_length=1
    )

    resident_country_code = models.CharField(
        verbose_name=_("Código País"),
        max_length=100
    )

    resident_country = models.CharField(
        verbose_name=_("Nome do País"),
        max_length=255
    )

    mother = models.CharField(
        verbose_name=_("Nome da Mãe"),
        max_length=255
    )

    birth_date = models.DateField(
        verbose_name=_("Data de Nasc"),
        null=True,
        blank=True
    )

    birth_country = models.CharField(
        verbose_name=_("Cód. País de Nasc."),
        max_length=3
    )

    birth_country_code = models.CharField(
        verbose_name=_("País de Nasc."),
        max_length=255
    )

    birth_province_code = models.CharField(
        verbose_name=_("Cód. Estado de Nasc."),
        max_length=3
    )

    birth_city = models.CharField(
        verbose_name=_("Natural de"),
        max_length=255
    )

    birth_city_code = models.CharField(
        verbose_name=_("Cód. Cidade de Nasc."),
        max_length=3
    )

    gender = models.IntegerField(
        verbose_name=_("Sexo"),
    )

    occupation_origin_code = models.CharField(
        verbose_name=_("Cód. da Natureza da Ocupação"),
        max_length=50
    )

    occupation_origin = models.CharField(
        verbose_name=_("Natureza da Ocupação"),
        max_length=255
    )

    main_occupation_code = models.CharField(
        verbose_name=_("Cód. Ocupação Principal"),
        max_length=50
    )

    main_occupation = models.CharField(
        verbose_name=_("Ocupação Principal"),
        max_length=255
    )

    occupation_current_year = models.CharField(
        verbose_name=_("Exercício da Ocupação"),
        max_length=50
    )

    administrative_unit = models.CharField(
        verbose_name=_("Unidade Administrativa"),
        max_length=255
    )

    administrative_unit_code = models.CharField(
        verbose_name=_("Cod. U. Administrativa"),
        max_length=10
    )

    address_type = models.CharField(
        verbose_name=_("Tipo de Logradouro"),
        max_length=255
    )

    address = models.CharField(
        verbose_name=_("Endereço"),
        max_length=255
    )

    address_number = models.CharField(
        verbose_name=_("Número"),
        max_length=50
    )

    address_complement = models.CharField(
        verbose_name=_("Complemento"),
        max_length=255
    )

    address_neighbor = models.CharField(
        verbose_name=_("Bairro"),
        max_length=255
    )

    address_zip = models.IntegerField(
        verbose_name=_("CEP"),
    )

    province_code = models.CharField(
        verbose_name=_("UF"),
        max_length=2
    )

    city_code = models.CharField(
        verbose_name=_("Código Município"),
        max_length=10
    )

    city = models.CharField(
        verbose_name=_("Município"),
        max_length=255
    )

    phone_code = models.CharField(
        verbose_name=_("DDD"),
        max_length=3
    )

    phone = models.CharField(
        verbose_name=_("Telefone"),
        max_length=16
    )

    death_date = models.CharField(
        verbose_name=_("Ano do Óbito"),
        max_length=4
    )

    stranger = models.CharField(
        verbose_name=_("Estrangeiro"),
        max_length=1
    )

    updated_at = models.DateField(
        verbose_name=_("Data de Atualização"),
    )

    created_at = models.DateField(
        verbose_name=_("Data de Inscrição"),
    )
