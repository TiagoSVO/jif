from django.db import models

from datetime import datetime

from core.models import JIF
from dept.models import Dept
from sex.models import Sex


# Create your models here.
class TeamStatus(models.Model):
    code = models.CharField(max_length=10, verbose_name="Código", blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Situação de Time'
        verbose_name_plural = 'Situações de Times'

    def __str__(self):
        return f'{self.title}'


class Team(models.Model):
    code = models.CharField(max_length=10, verbose_name="Código", unique=True)
    flag = models.ImageField(upload_to='flags', blank=True, null=True, verbose_name="Bandeira")
    title = models.CharField(max_length=100, verbose_name='Título')
    titular_member_quantity = models.IntegerField(verbose_name="Número de Integrantes Titulares")
    reserve_members_quantity = models.IntegerField(verbose_name="Número de Integrantes Reservas")
    description = models.TextField(verbose_name="Descrição")
    modality = models.ForeignKey('modality.Modality', on_delete=models.CASCADE, verbose_name="Modalidade")
    dept = models.ForeignKey("dept.Dept", on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campus')
    sex = models.ForeignKey("sex.Sex", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Sexo")
    team_status = models.ForeignKey("team.TeamStatus", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Situação do Time")
    # TODO: Os campos modalidade e sexo tem uma relação

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return f'{self.code} | {self.title}'


class JIFsTeam(models.Model):
    jif = models.ForeignKey(JIF, on_delete=models.CASCADE, verbose_name="JIF")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Time")
    team_status = models.ForeignKey("team.TeamStatus", on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Situação do Time")

    class Meta:
        verbose_name = 'Time de JIF'
        verbose_name_plural = 'Times de JIFs'

    def __str__(self):
        return f'{self.jif.title} | {self.team.title}'


class ChampionshipsTeam(models.Model):
    championship = models.ForeignKey('championship.Championship', on_delete=models.CASCADE, verbose_name="Campeonato")
    team = models.ForeignKey("team.JIFsTeam", on_delete=models.CASCADE, verbose_name="Time")

    class Meta:
        verbose_name = 'Time do Campeonato'
        verbose_name_plural = 'Times dos Campeonatos'

    def __str__(self):
        return f'{self.jif.title} | {self.team.title}'


class GameTeam(models.Model):
    game = models.ForeignKey("championship.Game", on_delete=models.CASCADE, verbose_name="Jogo")
    jif_team = models.ForeignKey("team.JIFsTeam", on_delete=models.CASCADE, verbose_name="Time do JIF")
    score = models.IntegerField(verbose_name="Pontuação")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Criado")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="Atualizado")
    updater_profile = models.ForeignKey('userjif.JIFUserProfile', on_delete=models.SET_NULL, blank=True, null=True) # Evitar circular import error

    class Meta:
        unique_together = ('game', 'jif_team',)
        verbose_name = 'Time em Jogo'
        verbose_name_plural = 'Times em Jogos'

