from django.db import models
from datetime import datetime


class JIFB(models.Model):
    title = models.CharField(max_length=80, verbose_name="Título")
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)
    year = models.IntegerField(verbose_name="Ano")
    edition = models.CharField(max_length=30, verbose_name="Edição")
    date_init = models.DateTimeField(default=datetime.now(), verbose_name="Início")
    date_end = models.DateTimeField(default=datetime.now(), verbose_name="Fim")

    class Meta:
        verbose_name = 'JIFB'
        verbose_name_plural = 'JIFBs'

    def __str__(self):
        return f'{self.title} - {self.year}/{self.edition}'


class Phone(models.Model):
    prefix = models.CharField(max_length=3, verbose_name='Prefixo')
    number = models.CharField(max_length=9, verbose_name='Número')

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return f'{self.number_formatted()}'

    def number_formatted(self):
        number = f'{self.number[0]}.{self.number[1:5]}-{self.number[5:]}' if len(self.number) > 8 else f'{self.number[0:4]}-{self.number[4:]}'
        return f'({self.prefix}) {number}'


class Dept(models.Model):
    title = models.CharField(max_length=80, verbose_name="Título")
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campi'

    def __str__(self):
        return f'{self.title}'


class Sex(models.Model):
    title = models.CharField(max_length=30, verbose_name="Sexo")
    acronym = models.CharField(max_length=2, verbose_name="Abreviação", blank=True, null=True)

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'

    def __str__(self):
        return f'{self.title}'


