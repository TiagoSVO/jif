from django.db import models
from core.models import JIF


class Committee(models.Model):
    jif = models.ForeignKey(JIF, on_delete=models.CASCADE, verbose_name="JIF")
    title = models.CharField(max_length=100, verbose_name="Nome da Comissão")
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Comissão'
        verbose_name_plural = 'Comissões'

    def __str__(self):
        return f'{self.title} | {self.jif.title} | {self.jif.year} | {self.jif.edition}'


class FunctionTypeCommittee(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nome da Função de Comissão")
    code = models.CharField(max_length=3, verbose_name="Código da Função de Comissão")
    description = models.TextField(verbose_name="Descrição da Função de  Comissão")

    class Meta:
        verbose_name = 'Função de Comissão'
        verbose_name_plural = 'Funções de Comissões'

    def __str__(self):
        return f'{self.title}'
