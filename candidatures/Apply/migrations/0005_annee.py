# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0004_auto_20150601_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('millesime', models.DateField(db_column='millesime', null=True, blank=True)),
                ('etablissement', models.CharField(db_column='etablissement', null=True, blank=True, max_length=100)),
                ('formation', models.CharField(db_column='formation', null=True, blank=True, max_length=100)),
                ('resultat', models.CharField(db_column='resultat', null=True, blank=True, max_length=30)),
                ('etudiant', models.ForeignKey(to='Apply.Etudiant')),
            ],
        ),
    ]
