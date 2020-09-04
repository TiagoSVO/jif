from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, siape, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        #TODO: Verificar login multiplo com email ou siape.
        if not siape:
            raise ValueError('É obrigatório o siape')
        email = self.normalize_email(email)
        user = self.model(siape=siape, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, siape, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(siape, email, password, **extra_fields)

    def create_superuser(self, siape, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O SuperUser precisa ter o is_superuser=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O SuperUser precisa ter o is_staff=True')

        return self._create_user(siape, email, password, **extra_fields)
