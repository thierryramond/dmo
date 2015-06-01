# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0005_annee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etudiant',
            options={'ordering': ('nom', 'prenom')},
        ),
        migrations.AlterField(
            model_name='annee',
            name='millesime',
            field=models.CharField(null=True, max_length=30, db_column='millesime', blank=True),
        ),
    ]
