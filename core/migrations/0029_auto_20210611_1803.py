# Generated by Django 3.1 on 2021-06-11 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20210611_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='athlete',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='jif_team',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='updater_profile',
        ),
        migrations.DeleteModel(
            name='Athlete',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
