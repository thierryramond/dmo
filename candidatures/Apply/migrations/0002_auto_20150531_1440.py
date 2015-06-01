# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='genre',
            field=models.CharField(null=True, blank=True, db_column='genre', choices=[('M.', 'M.'), ('Mme', 'Mme')], max_length=25),
        ),
    ]
