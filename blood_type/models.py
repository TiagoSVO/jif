from django.db import models


class BloodType(models.Model):
    title = models.CharField(max_length=3, verbose_name="Tipo Sanquíneo")

    class Meta:
        verbose_name = 'Tipo Sanguíneo'
        verbose_name_plural = 'Tipos Sanguíneos'

    def __str__(self):
        return f'{self.title}'
