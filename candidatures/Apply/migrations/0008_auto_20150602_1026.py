# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0007_auto_20150601_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidature',
            name='numero_OPI',
            field=models.CharField(null=True, max_length=10, blank=True, db_column='numero_OPI'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='carte_etudiant',
            field=models.CharField(null=True, max_length=10, blank=True, db_column='carte_etudiant'),
        ),
    ]
