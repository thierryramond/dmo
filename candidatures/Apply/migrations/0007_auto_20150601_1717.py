# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0006_auto_20150601_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='telephone',
            field=models.CharField(db_column='telephone', null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='confirmation',
            field=models.CharField(db_column='confirmation', null=True, max_length=50, choices=[('L3 MFA', 'L3 MFA'), ('L3 MINT', 'L3 MINT'), ('M1 MFA', 'M1 MFA'), ('Magistère 1', 'Magistère 1'), ('Magistère 2', 'Magistère 2'), ('Magistère 3', 'Magistère 3')], blank=True),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='demande',
            field=models.CharField(db_column='demande', null=True, max_length=50, choices=[('L3 MFA', 'L3 MFA'), ('L3 MINT', 'L3 MINT'), ('M1 MFA', 'M1 MFA'), ('Magistère 1', 'Magistère 1'), ('Magistère 2', 'Magistère 2'), ('Magistère 3', 'Magistère 3')], blank=True),
        ),
        migrations.AlterField(
            model_name='candidature',
            name='reponse',
            field=models.CharField(db_column='reponse', null=True, max_length=50, choices=[('L3 MFA', 'L3 MFA'), ('L3 MINT', 'L3 MINT'), ('M1 MFA', 'M1 MFA'), ('Magistère 1', 'Magistère 1'), ('Magistère 2', 'Magistère 2'), ('Magistère 3', 'Magistère 3')], blank=True),
        ),
    ]
