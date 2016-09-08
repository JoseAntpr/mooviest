# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20160902_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='backdrop',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
