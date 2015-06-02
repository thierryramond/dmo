# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0008_auto_20150602_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='carte_etudiant',
            field=models.CharField(db_column='carte_etudiant', blank=True, unique=True, max_length=10, null=True),
        ),
    ]
