# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('genre', models.CharField(db_column='genre', null=True, blank=True, max_length=25)),
                ('nom', models.CharField(db_column='Nom', null=True, blank=True, max_length=25)),
                ('prenom', models.CharField(db_column='Prenom', null=True, blank=True, max_length=28)),
                ('date_naissance', models.DateField(db_column='date_naissance', null=True, blank=True)),
                ('adresse', models.CharField(db_column='adresse', null=True, blank=True, max_length=100)),
                ('email', models.EmailField(db_column='email', unique=True, null=True, blank=True, max_length=254)),
                ('vient_de', models.CharField(db_column='vient_de', null=True, blank=True, max_length=150)),
            ],
        ),
    ]
