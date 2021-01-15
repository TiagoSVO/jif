import re
import socket

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.mail import send_mail

from .managers import UserManager

from core.models import Sex, Dept, Committee, FunctionTypeCommittee


class JIFProfile(Group):
    description = models.TextField(verbose_name="Descrição do perfil", blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return f'{self.name}'


class User(AbstractBaseUser, PermissionsMixin):
    readonly_fields = [
        'date_joined',
    ]
    username = None

    siape = models.CharField(max_length=7, verbose_name="Siape", unique=True,
                             help_text='Requer 7 digitos numéricos.',
                             validators=[
                                 validators.RegexValidator(
                                     re.compile('^[0-9]'),
                                     'Digite um Siape válido!',
                                     'invalid'
                                 )
                             ])
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
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    email = models.EmailField(max_length=255, verbose_name='E-mail', unique=True)
    is_staff = models.BooleanField(default=True, verbose_name='Servidor(a)')
    is_active = models.BooleanField(default=True, verbose_name='Está ativo(a)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado hein')
    last_sign_in_ip = models.CharField(max_length=100, verbose_name='Último IP logado', blank=True, null=True)
    last_sign_in_at = models.DateTimeField(verbose_name='Último acesso em', blank=True, null=True)
    current_sign_in_ip = models.CharField(max_length=100, verbose_name='IP logado atual', blank=True, null=True)
    current_sign_in_at = models.DateTimeField(verbose_name='Acesso atual', blank=True, null=True)
    sex = models.ForeignKey(Sex, verbose_name="Sexo", blank=True, null=True, on_delete=models.SET_NULL)
    dept = models.ForeignKey(Dept, verbose_name="Campus", blank=True, null=True, on_delete=models.SET_NULL)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Ingresso em')
    jif_profiles = models.ManyToManyField(
        JIFProfile,
        verbose_name="Perfis",
        blank=True,
        help_text="O perfil é um conjunto de permissões que o usuário pode estar associado",
        related_name="user",
        through='JIFUserProfile',
    )

    USERNAME_FIELD = 'siape'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'cpf']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return f'{self.siape} - {self.first_name}'

    @staticmethod
    def _set_user_ip():
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return f'{ip_address} - {hostname}'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'siape',
                'is_superuser',
                'user_permissions',
            }

        if (
                not is_superuser
                and obj is not None
                and obj == request.user
        ):
            disabled_fields |= {
                'is_staff',
                'is_superuser',
                'user_permissions',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class JIFUserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    profile = models.ForeignKey(JIFProfile, on_delete=models.CASCADE, verbose_name="Perfil")
    dept = models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Campus")
    function_committees = models.ManyToManyField(
        FunctionTypeCommittee,
        verbose_name="Função da Comissão",
        blank=True,
        help_text="Este campo serve para informar qual função em determinada comissão é exercida",
        related_name="function_type_committee",
        through='FunctionTypeCommitteeUserProfile',
    )

    class Meta:
        verbose_name = 'Perfil de Usuário'
        verbose_name_plural = 'Perfis de Usuários'

    def __str__(self):
        return f'({self.user.siape}) {self.user.get_full_name()} | {self.profile.name}{" - " + self.dept.title if self.dept else ""}'

    def save(self, *args, **kwargs):
        print(self)
        if not self.dept:
            if self.user.dept:
                self.dept = self.user.dept
        super(JIFUserProfile, self).save(*args, **kwargs)


class FunctionTypeCommitteeUserProfile(models.Model):
    user_profile = models.ForeignKey(JIFUserProfile, on_delete=models.CASCADE, verbose_name="Perfil de Usuário")
    committee = models.ForeignKey(Committee, on_delete=models.CASCADE, verbose_name="Comissão")
    function_type_committee = models.ForeignKey(FunctionTypeCommittee, on_delete=models.CASCADE, verbose_name="Função da Comissão")

    class Meta:
        verbose_name = 'Função de Comissão'
        verbose_name_plural = 'Funções de Comissões'

    def __str__(self):
        return f'({self.committee.title} | {self.function_type_committee.title} | {self.user_profile.user.siape}) {self.user_profile.user.get_full_name()} | {self.profile.name}{" - " + self.dept.title if self.dept else ""}'