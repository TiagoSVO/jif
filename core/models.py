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

    class Meta:
        verbose_name = 'JIF'
        verbose_name_plural = 'JIFs'

    def __str__(self):
        return f'{self.title} - {self.year}/{self.edition}'


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


class Committee(models.Model):
    jif = models.ForeignKey(JIF, on_delete=models.CASCADE, verbose_name="JIF")
    title = models.CharField(max_length=100, verbose_name="Nome da Comissão")
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Comissão'
        verbose_name_plural = 'Comissões'

    def __str__(self):
        return f'{self.title} | {self.jif.title} | {self.jif.year} | {self.jif.edition}'


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


class Sex(models.Model):
    title = models.CharField(max_length=30, verbose_name="Sexo")
    acronym = models.CharField(max_length=2, verbose_name="Abreviação", blank=True, null=True)

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexos'

    def __str__(self):
        return f'{self.title}'


class BloodType(models.Model):
    title = models.CharField(max_length=3, verbose_name="Tipo Sanquíneo")

    class Meta:
        verbose_name = 'Tipo Sanguíneo'
        verbose_name_plural = 'Tipos Sanguíneos'

    def __str__(self):
        return f'{self.title}'


class ModalityType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Tipo de Modalidade'
        verbose_name_plural = 'Tipos de Modalidades'

    def __str__(self):
        return f'{self.title}'


class Modality(models.Model):
    modality_type = models.ForeignKey(ModalityType, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")
    sex = models.ForeignKey(Sex,  on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return f'{self.modality_type.title} | {self.title}'


class Championship(models.Model):
    #TODO: Modificar de jif para jif_modality
    jif = models.ForeignKey(JIF, on_delete=models.CASCADE, verbose_name="JIF")
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name="Descrição")
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonato'

    def __str__(self):
        return f'{self.title} - {self.jif.title}'


class Group(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, verbose_name="JIF")
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name="Descrição")
    unique = models.BooleanField(verbose_name="Grupo único do campeonato?")

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return f'{self.title} - {self.championship.title}'


class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name="Descrição")
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, verbose_name="JIF")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="JIF")

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

    def __str__(self):
        return f'{self.title} - {self.group.title} - {self.championship.title}'
