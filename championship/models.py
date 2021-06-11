from django.db import models


class Championship(models.Model):
    jif_modality = models.ForeignKey('modality.JIFModality', on_delete=models.CASCADE, verbose_name="Modalidade")
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name="Descrição")
    started_at = models.DateTimeField(verbose_name="Início")
    finished_at = models.DateTimeField(verbose_name="Fim")
    teams = models.ManyToManyField('team.JIFsTeam', through='team.ChampionshipsTeam', related_name='csteams', blank=True, verbose_name="Times")

    class Meta:
        verbose_name = 'Campeonato'
        verbose_name_plural = 'Campeonato'

    def __str__(self):
        return f'{self.title} - {self.jif.title}'


class Group(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, verbose_name="Campeonato")
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
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, verbose_name="Campeonato")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Grupo")

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

    def __str__(self):
        return f'{self.title} - {self.group.title} - {self.championship.title}'
