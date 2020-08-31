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


