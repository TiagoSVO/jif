# Generated by Django 3.1 on 2020-12-11 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userjif', '0002_auto_20201211_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='jif_profiles',
            field=models.ManyToManyField(blank=True, help_text='O perfil é um conjunto de permissões que o usuário pode estar associado', related_name='user', through='userjif.JIFUserProfile', to='userjif.JIFProfile', verbose_name='Perfis'),
        ),
    ]
