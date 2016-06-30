# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20160630_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_producer',
            field=models.CharField(max_length=255),
        ),
    ]
