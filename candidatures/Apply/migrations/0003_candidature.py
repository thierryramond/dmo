# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0002_auto_20150531_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('millesime', models.DateField(null=True, blank=True, db_column='millesime')),
                ('demande', models.CharField(null=True, max_length=50, blank=True, choices=[('L3 MFA', 'L3 MFA'), ('L3 MINT', 'L3 MINT'), ('M1 MFA', 'M1 MFA'), ('Magistère1', 'Magistère1')], db_column='demande')),
                ('reponse', models.CharField(null=True, max_length=50, blank=True, choices=[('L3 MFA', 'L3 MFA'), ('L3 MINT', 'L3 MINT'), ('M1 MFA', 'M1 MFA'), ('Magistère1', 'Magistère1')], db_column='reponse')),
                ('confirmation', models.CharField(null=True, max_length=50, blank=True, choices=[('L3 MFA', 'L3 MFA'), ('L3 MINT', 'L3 MINT'), ('M1 MFA', 'M1 MFA'), ('Magistère1', 'Magistère1')], db_column='confirmation')),
                ('reponse_donnee_par', models.CharField(null=True, max_length=50, blank=True, choices=[('Dominique Hulin', 'Dominique Hulin'), ('Marie-Anne Poursat', 'Marie-Anne Poursat')], db_column='reponse_donnee_par')),
                ('date_reponse', models.DateField(null=True, blank=True, db_column='date_reponse')),
                ('etudiant', models.ForeignKey(to='Apply.Etudiant')),
            ],
        ),
    ]
