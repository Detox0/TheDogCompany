# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-18 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theDogCompany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='persona',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='theDogCompany.Persona'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carnet',
            name='persona',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='theDogCompany.Persona'),
            preserve_default=False,
        ),
    ]
