from django.db import models
from datetime import datetime
from core.models import JIF


class JIFsEvent(models.Model):
    jif = models.ForeignKey(JIF, on_delete=models.CASCADE, verbose_name='JIF')
    title = models.CharField(max_length=80, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição", blank=True, null=True)
    date_init = models.DateTimeField(default=datetime.now, verbose_name="Início")
    date_end = models.DateTimeField(default=datetime.now, verbose_name="Fim")
    image = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return f'{self.title} | {self.jif.title}'
