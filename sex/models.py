from django.db import models


class Sex(models.Model):
    title = models.CharField(max_length=30, verbose_name="Sexo")
    acronym = models.CharField(max_length=2, verbose_name="Abreviação", blank=True, null=True)

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'

    def __str__(self):
        return f'{self.title}'
