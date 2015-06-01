# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0003_candidature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidature',
            name='millesime',
        ),
        migrations.AddField(
            model_name='candidature',
            name='date_demande',
            field=models.DateField(db_column='date_demande', null=True, blank=True),
        ),
    ]
