# Generated by Django 3.1 on 2021-01-21 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20210121_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jifmodality',
            name='jif',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.jif'),
        ),
        migrations.AlterField(
            model_name='jifmodality',
            name='modality',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.modality'),
        ),
        migrations.AlterField(
            model_name='jifsteam',
            name='jif',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.jif'),
        ),
        migrations.AlterField(
            model_name='jifsteam',
            name='team',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.team'),
        ),
    ]
