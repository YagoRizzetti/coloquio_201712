# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=128, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=128, verbose_name='Apellido')),
                ('dni', models.PositiveIntegerField(verbose_name='DNI')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='T\xedtulo')),
                ('docente', models.CharField(max_length=128, verbose_name='Docente')),
                ('carga_horaria', models.PositiveIntegerField(verbose_name='Carga Horaria')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='academico.Alumno')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnos', to='academico.Asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.PositiveIntegerField(verbose_name='Valor')),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='academico.Matricula')),
            ],
        ),
    ]