from django.db import models


class Phone(models.Model):
    prefix = models.CharField(max_length=3, verbose_name='Prefixo', default='XX')
    number = models.CharField(max_length=9, verbose_name='Número', default='XXXXXXXXX')

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'
        abstract = True

    def __str__(self):
        return f'{self.number_formatted}'

    @property
    def number_formatted(self):
        number = f'{self.number[0]}.{self.number[1:5]}-{self.number[5:]}' if len(self.number) > 8 else f'{self.number[0:4]}-{self.number[4:]}'
        return f'({self.prefix}) {number}'