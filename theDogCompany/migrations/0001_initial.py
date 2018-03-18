# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-18 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('patente', models.CharField(blank=True, max_length=10)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Carnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaVencimiento', models.DateField()),
                ('numeroSerie', models.CharField(max_length=10)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoPaterno', models.CharField(max_length=50)),
                ('apellidoMaterno', models.CharField(max_length=50)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
    ]