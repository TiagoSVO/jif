from django.db import models
from sex.models import Sex


class ScoreType(models.Model):
    code = models.CharField(max_length=10, verbose_name="Código")
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Tipo de Pontuação'
        verbose_name_plural = 'Tipos de Pontuações'

    def __str__(self):
        return f'{self.title}'


class ModalityGrouping(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    acronym = models.CharField(max_length=1, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Agrupamento de Modalidade'
        verbose_name_plural = 'Agrupamentos de Modalidades'

    def __str__(self):
        return f'{self.title}'


class ModalityType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")
    score_type = models.ForeignKey(ScoreType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Tipo de Pontuação")

    class Meta:
        verbose_name = 'Tipo de Modalidade'
        verbose_name_plural = 'Tipos de Modalidades'

    def __str__(self):
        return f'{self.title}'


class Modality(models.Model):
    modality_type = models.ForeignKey(ModalityType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Tipo de Modalidade')
    title = models.CharField(max_length=100, verbose_name='Título')
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")
    sex = models.ForeignKey(Sex,  on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sexo')
    grouping = models.ForeignKey(ModalityGrouping, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Agrupamento')

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return f'{self.modality_type.title} | {self.title}'


class JIFModality(models.Model):
    jif = models.ForeignKey('core.JIF', on_delete=models.CASCADE, verbose_name="JIF")
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE, verbose_name="Modalidade")

    class Meta:
        verbose_name = 'Modalidade do JIF'
        verbose_name_plural = 'Modalidades dos JIFS'

    def __str__(self):
        jif_label = self.jif.acronym or self.jif.title
        return f'{jif_label} | {self.modality.modality_type.title} - {self.modality.title}'
