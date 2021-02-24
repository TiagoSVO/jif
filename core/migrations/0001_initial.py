# Generated by Django 3.1 on 2021-02-23 14:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3, verbose_name='Tipo Sanquíneo')),
            ],
            options={
                'verbose_name': 'Tipo Sanguíneo',
                'verbose_name_plural': 'Tipos Sanguíneos',
            },
        ),
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Campeonato',
                'verbose_name_plural': 'Campeonato',
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('acronym', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abreviação')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campi',
            },
        ),
        migrations.CreateModel(
            name='FunctionTypeCommittee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nome da Função de Comissão')),
                ('code', models.CharField(max_length=3, verbose_name='Código da Função de Comissão')),
                ('description', models.TextField(verbose_name='Descrição da Função de  Comissão')),
            ],
            options={
                'verbose_name': 'Função de Comissão',
                'verbose_name_plural': 'Funções de Comissões',
            },
        ),
        migrations.CreateModel(
            name='GameTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='JIF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('acronym', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abreviação')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('year', models.IntegerField(verbose_name='Ano')),
                ('edition', models.CharField(max_length=30, verbose_name='Edição')),
                ('date_init', models.DateTimeField(default=datetime.datetime.now, verbose_name='Início')),
                ('date_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fim')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
            ],
            options={
                'verbose_name': 'JIF',
                'verbose_name_plural': 'JIFs',
            },
        ),
        migrations.CreateModel(
            name='JIFModality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jif')),
            ],
            options={
                'verbose_name': 'Modalidade do JIF',
                'verbose_name_plural': 'Modalidades dos JIFS',
            },
        ),
        migrations.CreateModel(
            name='JIFModalityRestriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jif_modality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jifmodality')),
            ],
            options={
                'verbose_name': 'Restrição de Modalidade do JIF',
                'verbose_name_plural': 'Restrições de Modalidades dos JIFS',
            },
        ),
        migrations.CreateModel(
            name='Modality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('acronym', models.CharField(blank=True, max_length=10, null=True, verbose_name='Abreviação')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Modalidade',
                'verbose_name_plural': 'Modalidades',
            },
        ),
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
            name='Restriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Restrição',
                'verbose_name_plural': 'Restrições',
            },
        ),
        migrations.CreateModel(
            name='ScoreType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Score',
                'verbose_name_plural': 'Tipos de Scores',
            },
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Sexo')),
                ('acronym', models.CharField(blank=True, max_length=2, null=True, verbose_name='Abreviação')),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
            },
        ),
        migrations.CreateModel(
            name='TeamStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Código')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Situação de Time',
                'verbose_name_plural': 'Situações de Times',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('flag', models.ImageField(blank=True, null=True, upload_to='flags')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('titular_member_quantity', models.IntegerField(verbose_name='Número de Integrantes Titulares')),
                ('reserve_members_quantity', models.IntegerField(verbose_name='Número de Integrantes Reservas')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.dept', verbose_name='Campus')),
                ('modality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modality')),
                ('sex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sex')),
                ('team_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.teamstatus')),
            ],
            options={
                'verbose_name': 'Time',
                'verbose_name_plural': 'Times',
            },
        ),
        migrations.AddField(
            model_name='modality',
            name='modality_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.modalitytype'),
        ),
        migrations.AddField(
            model_name='modality',
            name='sex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.sex'),
        ),
        migrations.CreateModel(
            name='JIFsTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jif')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
            ],
            options={
                'verbose_name': 'Time de JIF',
                'verbose_name_plural': 'Times de JIFs',
            },
        ),
        migrations.CreateModel(
            name='JIFsEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('date_init', models.DateTimeField(default=datetime.datetime.now, verbose_name='Início')),
                ('date_end', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fim')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('jif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jif', verbose_name='JIF')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='JIFModalityRestrictionValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, help_text='Campo opicional para atribuir algum valor', max_length=100, null=True, verbose_name='Valor para restrição')),
                ('jif_modality_restriction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jifmodalityrestriction')),
            ],
            options={
                'verbose_name': 'Valor de Restrição para modalidade',
                'verbose_name_plural': 'Valores de Restrições para modalidades',
            },
        ),
        migrations.AddField(
            model_name='jifmodalityrestriction',
            name='restriction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.restriction'),
        ),
        migrations.AddField(
            model_name='jifmodality',
            name='modality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modality'),
        ),
        migrations.AddField(
            model_name='jif',
            name='modalities',
            field=models.ManyToManyField(blank=True, related_name='modalities', through='core.JIFModality', to='core.Modality'),
        ),
        migrations.AddField(
            model_name='jif',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='teams', through='core.JIFsTeam', to='core.Team'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('unique', models.BooleanField(verbose_name='Grupo único do campeonato?')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.championship', verbose_name='JIF')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.championship', verbose_name='JIF')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.group', verbose_name='JIF')),
            ],
            options={
                'verbose_name': 'Jogo',
                'verbose_name_plural': 'Jogos',
            },
        ),
        migrations.CreateModel(
            name='DeptsPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(default='XX', max_length=3, verbose_name='Prefixo')),
                ('number', models.CharField(default='XXXXXXXXX', max_length=9, verbose_name='Número')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dept', verbose_name='Campus')),
            ],
            options={
                'verbose_name': 'Telefone do Campus',
                'verbose_name_plural': 'Telefones dos Campi',
            },
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nome da Comissão')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('jif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jif', verbose_name='JIF')),
            ],
            options={
                'verbose_name': 'Comissão',
                'verbose_name_plural': 'Comissões',
            },
        ),
        migrations.CreateModel(
            name='ChampionshipsTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('championship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.championship')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
            ],
            options={
                'verbose_name': 'Time do Campeonato',
                'verbose_name_plural': 'Times dos Campeonatos',
            },
        ),
        migrations.AddField(
            model_name='championship',
            name='jif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.jif', verbose_name='JIF'),
        ),
        migrations.AddField(
            model_name='championship',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='csteams', through='core.ChampionshipsTeam', to='core.Team'),
        ),
    ]
