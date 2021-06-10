# Generated by Django 3.1 on 2021-06-10 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0001_initial'),
        ('userjif', '0003_jifprofile_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='functiontypecommitteeuserprofile',
            name='committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='committee.committee', verbose_name='Comissão'),
        ),
        migrations.AlterField(
            model_name='functiontypecommitteeuserprofile',
            name='function_type_committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='committee.functiontypecommittee', verbose_name='Função da Comissão'),
        ),
        migrations.AlterField(
            model_name='jifuserprofile',
            name='function_committees',
            field=models.ManyToManyField(blank=True, help_text='Este campo serve para informar qual função em determinada comissão é exercida', related_name='function_type_committee', through='userjif.FunctionTypeCommitteeUserProfile', to='committee.FunctionTypeCommittee', verbose_name='Função da Comissão'),
        ),
    ]
