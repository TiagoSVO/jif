# Generated by Django 3.1 on 2020-09-04 17:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3, verbose_name='Tipo Sanquíneo')),
            ],
            options={
                'verbose_name': 'Tipo Sanguíneo',
                'verbose_name_plural': 'Tipos Sanguíneos',
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('acronym', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abreviação')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campi',
            },
        ),
        migrations.CreateModel(
            name='JIF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('acronym', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abreviação')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('year', models.IntegerField(verbose_name='Ano')),
                ('edition', models.CharField(max_length=30, verbose_name='Edição')),
                ('date_init', models.DateTimeField(default=datetime.datetime.now, verbose_name='Início')),
                ('date_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fim')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
            ],
            options={
                'verbose_name': 'JIF',
                'verbose_name_plural': 'JIFs',
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Sexo')),
                ('acronym', models.CharField(blank=True, max_length=2, null=True, verbose_name='Abreviação')),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
            },
        ),
        migrations.CreateModel(
            name='JIFsEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('date_init', models.DateTimeField(default=datetime.datetime.now, verbose_name='Início')),
                ('date_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fim')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('jif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jif', verbose_name='JIF')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='DeptsPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(default='XX', max_length=3, verbose_name='Prefixo')),
                ('number', models.CharField(default='XXXXXXXXX', max_length=9, verbose_name='Número')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dept', verbose_name='Campus')),
            ],
            options={
                'verbose_name': 'Telefone do Campus',
                'verbose_name_plural': 'Telefones dos Campi',
            },
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nome da Comissão')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('jif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jif', verbose_name='JIF')),
            ],
            options={
                'verbose_name': 'Comissão',
                'verbose_name_plural': 'Comissões',
            },
        ),
    ]
