# Generated by Django 3.1 on 2020-08-31 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200831_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='acronym',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Abreviação'),
        ),
        migrations.AlterField(
            model_name='jifb',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 31, 11, 16, 10, 205584), verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='jifb',
            name='date_init',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 31, 11, 16, 10, 205584), verbose_name='Início'),
        ),
    ]