# Generated by Django 3.1 on 2021-05-05 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210427_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='championship',
            name='finished_at',
            field=models.DateTimeField(verbose_name='Fim'),
        ),
        migrations.AlterField(
            model_name='championship',
            name='jif_modality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jifmodality', verbose_name='Modalidade'),
        ),
        migrations.AlterField(
            model_name='championship',
            name='started_at',
            field=models.DateTimeField(verbose_name='Início'),
        ),
        migrations.AlterField(
            model_name='championship',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='csteams', through='core.ChampionshipsTeam', to='core.JIFsTeam', verbose_name='Times'),
        ),
    ]
