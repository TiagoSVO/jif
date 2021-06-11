from django.db import models


class Restriction(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    code = models.CharField(max_length=10, verbose_name="Código", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Restrição'
        verbose_name_plural = 'Restrições'

    def __str__(self):
        return f'{self.title}'


class JIFModalityRestriction(models.Model):
    jif_modality = models.ForeignKey('modality.JIFModality', on_delete=models.CASCADE, verbose_name="Modalidade do JIF")
    restriction = models.ForeignKey(Restriction, on_delete=models.CASCADE, verbose_name="Restrição")

    class Meta:
        verbose_name = 'Restrição de Modalidade do JIF'
        verbose_name_plural = 'Restrições de Modalidades dos JIFS'

    def __str__(self):
        return f'{self.jif_modality.jif.title} | {self.jif_modality.modality.title}'


class JIFModalityRestrictionValue(models.Model):
    jif_modality_restriction = models.ForeignKey(JIFModalityRestriction, on_delete=models.CASCADE)
    value = models.CharField(max_length=100, verbose_name='Valor para restrição',
                             help_text='Campo opicional para atribuir algum valor', blank=True, null=True)

    class Meta:
        verbose_name = 'Valor de Restrição para modalidade'
        verbose_name_plural = 'Valores de Restrições para modalidades'

    def __str__(self):
        return f'{self.jif_modality_restriction.restriction.title} | {self.value}'
