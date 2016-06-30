# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20160630_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='duration',
        ),
        migrations.AddField(
            model_name='movie',
            name='runtime',
            field=models.IntegerField(default=1, blank=True),
        ),
    ]
