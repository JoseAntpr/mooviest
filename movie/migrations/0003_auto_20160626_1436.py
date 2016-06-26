# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20160626_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='saga',
            field=models.ForeignKey(blank=True, null=True, to='movie.Saga'),
        ),
    ]
