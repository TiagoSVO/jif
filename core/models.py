import re

from datetime import datetime

from django.core import validators
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
    modalities = models.ManyToManyField('Modality', through='JIFModality', related_name='modalities', blank=True)
    teams = models.ManyToManyField('Team', through='JIFsTeam', related_name='teams', blank=True)

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


class FunctionTypeCommittee(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nome da Função de Comissão")
    code = models.CharField(max_length=3, verbose_name="Código da Função de Comissão")
    description = models.TextField(verbose_name="Descrição da Função de  Comissão")

    class Meta:
        verbose_name = 'Função de Comissão'
        verbose_name_plural = 'Funções de Comissões'

    def __str__(self):
        return f'{self.title}'


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


class ScoreType(models.Model):
    code = models.CharField(max_length=10, verbose_name="Código")
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = 'Tipo de Score'
        verbose_name_plural = 'Tipos de Scores'

    def __str__(self):
        return f'{self.title}'


class ModalityType(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    acronym = models.CharField(max_length=10, verbose_name="Abreviação", blank=True, null=True)
    description = models.TextField(verbose_name="Descrição")
    score_type = models.ForeignKey(ScoreType, on_delete=models.SET_NULL, blank=True, null=True)

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


class JIFModality(models.Model):
    jif = models.ForeignKey(JIF, on_delete=models.CASCADE)
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Modalidade do JIF'
        verbose_name_plural = 'Modalidades dos JIFS'

    def __str__(self):
        jif_label = self.jif.acronym or self.jif.title
        return f'{jif_label} | {self.modality.modality_type.title} - {self.modality.title}'


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
    jif_modality = models.ForeignKey(JIFModality, on_delete=models.CASCADE)
    restriction = models.ForeignKey(Restriction, on_delete=models.CASCADE)

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


class Championship(models.Model):
    jif_modality = models.ForeignKey(JIFModality, on_delete=models.CASCADE, verbose_name="Modalidade")
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name="Descrição")
    started_at = models.DateTimeField(verbose_name="Início")
    finished_at = models.DateTimeField(verbose_name="Fim")
    teams = models.ManyToManyField('JIFsTeam', through='ChampionshipsTeam', related_name='csteams', blank=True, verbose_name="Times")

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
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE, verbose_name="JIF")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="JIF")

    class Meta:
        verbose_name = 'Jogo'
        verbose_name_plural = 'Jogos'

    def __str__(self):
        return f'{self.title} - {self.group.title} - {self.championship.title}'


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
    flag = models.ImageField(upload_to='flags', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Título')
    titular_member_quantity = models.IntegerField(verbose_name="Número de Integrantes Titulares")
    reserve_members_quantity = models.IntegerField(verbose_name="Número de Integrantes Reservas")
    description = models.TextField(verbose_name="Descrição")
    modality = models.ForeignKey(Modality, on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Campus')
    sex = models.ForeignKey(Sex, on_delete=models.SET_NULL, blank=True, null=True)
    team_status = models.ForeignKey(TeamStatus, on_delete=models.SET_NULL, blank=True, null=True)
    # TODO: Os campos modalidade e sexo tem uma relação

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return f'{self.code} | {self.title}'


class JIFsTeam(models.Model):
    jif = models.ForeignKey(JIF, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_status = models.ForeignKey(TeamStatus, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Time de JIF'
        verbose_name_plural = 'Times de JIFs'

    def __str__(self):
        return f'{self.jif.title} | {self.team.title}'


class ChampionshipsTeam(models.Model):
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)
    team = models.ForeignKey(JIFsTeam, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Time do Campeonato'
        verbose_name_plural = 'Times dos Campeonatos'

    def __str__(self):
        return f'{self.jif.title} | {self.team.title}'


class GameTeam(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    jif_team = models.ForeignKey(JIFsTeam, on_delete=models.CASCADE)
    score = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now, verbose_name="Criado")
    updated_at = models.DateTimeField(default=datetime.now, verbose_name="Atualizado")
    updater_profile = models.ForeignKey('userjif.JIFUserProfile', on_delete=models.SET_NULL, blank=True, null=True) # Evitar circular import error

    class Meta:
        unique_together = ('game', 'jif_team',)
        verbose_name = 'Time em Jogo'
        verbose_name_plural = 'Times em Jogos'


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
    jif_team = models.ForeignKey(JIFsTeam, on_delete=models.CASCADE, verbose_name="Time")
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


