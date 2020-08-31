from django.db import models
from datetime import datetime


class JIFB(models.Model):
    title = models.CharField(max_length=80, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    year = models.IntegerField(verbose_name="Ano")
    edition = models.CharField(max_length=30, verbose_name="Edição")
    date_init = models.DateTimeField(default=datetime.now(), verbose_name="Início")
    date_end = models.DateTimeField(default=datetime.now(), verbose_name="Fim")

    def __str__(self):
        return f'{self.title} - {self.year}/{self.edition}'


class Phone(models.Model):
    prefix = models.CharField(max_length=3)
    number = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.number_formatted()}'

    def number_formatted(self):
        number = f'{self.number[0]}.{self.number[1:5]}-{self.number[5:]}' if len(self.number) > 8 else f'{self.number[0:4]}-{self.number[4:]}'
        return f'({self.prefix}) {number}'
