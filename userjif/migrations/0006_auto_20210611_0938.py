# Generated by Django 3.1 on 2021-06-11 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sex', '0001_initial'),
        ('userjif', '0005_auto_20210610_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sex.sex', verbose_name='Sexo'),
        ),
    ]