# Generated by Django 3.1 on 2021-06-11 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood_type', '0001_initial'),
        ('core', '0022_auto_20210611_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='blood_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blood_type.bloodtype', verbose_name='Tipo Sanguíneo'),
        ),
        migrations.DeleteModel(
            name='BloodType',
        ),
    ]