# Generated by Django 3.1 on 2021-06-10 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dept', '0001_initial'),
        ('userjif', '0004_auto_20210610_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jifuserprofile',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dept.dept', verbose_name='Campus'),
        ),
        migrations.AlterField(
            model_name='user',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dept.dept', verbose_name='Campus'),
        ),
    ]
