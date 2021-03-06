# Generated by Django 3.1 on 2020-09-22 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200917_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModalityType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('acronym', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abreviação')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Modalidade',
                'verbose_name_plural': 'Tipos de Modalidades',
            },
        ),
        migrations.CreateModel(
            name='Modality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('acronym', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abreviação')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('modality_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.modalitytype')),
                ('sex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sex')),
            ],
            options={
                'verbose_name': 'Modalidade',
                'verbose_name_plural': 'Modalidades',
            },
        ),
    ]
