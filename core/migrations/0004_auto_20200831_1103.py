# Generated by Django 3.1 on 2020-08-31 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200831_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=3)),
                ('number', models.CharField(max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='jifb',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 31, 11, 3, 55, 909530), verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='jifb',
            name='date_init',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 31, 11, 3, 55, 909530), verbose_name='Início'),
        ),
    ]
