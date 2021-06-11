from datetime import datetime

from django.db import models


class JIF(models.Model):
    title = models.CharField(max_length=80, verbose_name="Título")
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)
    year = models.IntegerField(verbose_name="Ano")
    edition = models.CharField(max_length=30, verbose_name="Edição")
    date_init = models.DateTimeField(default=datetime.now, verbose_name="Início")
    date_end = models.DateTimeField(default=datetime.now, verbose_name="Fim")
    image = models.ImageField(upload_to='products', blank=True, null=True)
    modalities = models.ManyToManyField('modality.Modality', through='modality.JIFModality', related_name='modalities', blank=True)
    teams = models.ManyToManyField('team.Team', through='team.JIFsTeam', related_name='teams', blank=True)

    class Meta:
        verbose_name = 'JIF'
        verbose_name_plural = 'JIFs'

    def __str__(self):
        return f'{self.title} - {self.year}/{self.edition}'
