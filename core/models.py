import re

from datetime import datetime

from django.core import validators
from django.db import models
from dept.models import Dept
from sex.models import Sex
from blood_type.models import BloodType


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


class Athlete(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    cpf = models.CharField(max_length=11, verbose_name="CPF", unique=True,
                           help_text='Digite apenas 11 digitos numéricos.',
                           validators=[
                               validators.RegexValidator(
                                   re.compile('^[0-9]'),
                                   'Digite um CPF válido!',
                                   'invalid'
                               )
                           ])
    rg = models.CharField(max_length=20, verbose_name="RG", unique=True,
                          validators=[
                              validators.RegexValidator(
                                  re.compile('^[0-9]'),
                                  'Digite um RG válido!',
                                  'invalid'
                              )
                          ], blank=True, null=True)
    email = models.EmailField(max_length=255, verbose_name='E-mail', unique=True)
    registration = models.CharField(max_length=11, verbose_name="Matrícula", unique=True) #TODO: Terminar esta parte e depois ver anotação do Google Drive docs
    birth_date = models.DateField(verbose_name="Data de Aniversário")
    health_care = models.CharField(max_length=30, verbose_name="Plano de Saúde", blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Criado")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="Atualizado")
    sus_number = models.CharField(max_length=15, verbose_name="N° do SUS", blank=True, null=True)
    photo = models.ImageField(upload_to='athletes', blank=True, null=True, verbose_name="Foto")
    medicine = models.TextField(verbose_name="Medicamentos", blank=True, null=True)
    active = models.BooleanField(verbose_name="Atleta ativo?")
    sex = models.ForeignKey(Sex, verbose_name="Sexo", blank=True, null=True, on_delete=models.SET_NULL)
    dept = models.ForeignKey(Dept, verbose_name="Campus", blank=True, null=True, on_delete=models.SET_NULL)
    blood_type = models.ForeignKey(BloodType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Tipo Sanguíneo")
    updater_profile = models.ForeignKey('userjif.JIFUserProfile', on_delete=models.SET_NULL, blank=True, null=True) # 'userjif.JIFUserProfile' -> Evitar circular import error

    class Meta:
        verbose_name = 'Atleta'
        verbose_name_plural = 'Atletas'

    def __str__(self):
        return f'{self.complete_name()}'

    def complete_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now
        super(Athlete, self).save(*args, **kwargs)


class Subscription(models.Model):
    jif_team = models.ForeignKey("team.JIFsTeam", on_delete=models.CASCADE, verbose_name="Time")
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, verbose_name="Atleta")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Criado")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="Atualizado")
    updater_profile = models.ForeignKey('userjif.JIFUserProfile', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Perfil de Atualização do Usuário")  # Evitar circular import error

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'

    def __str__(self):
        return f'{self.athlete.first_name} | {self.jif_team.team.title} | {self.jif_team.jif.title} - {self.jif_team.jif.year}'

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now
        super(Subscription, self).save(*args, **kwargs)
