# Generated by Django 3.1 on 2020-08-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JIFB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('year', models.IntegerField(verbose_name='Ano')),
                ('edition', models.CharField(max_length=30, verbose_name='Edição')),
            ],
        ),
    ]