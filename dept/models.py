from django.db import models
from phone.models import Phone


class Dept(models.Model):
    title = models.CharField(max_length=80, verbose_name="Título")
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Campus'
        verbose_name_plural = 'Campi'

    def __str__(self):
        return f'{self.title}'


class DeptsPhone(Phone):
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, verbose_name='Campus')

    class Meta:
        verbose_name = 'Telefone do Campus'
        verbose_name_plural = 'Telefones dos Campi'

    def __str__(self):
        return f'{self.dept.title} - {self.number_formatted}'
