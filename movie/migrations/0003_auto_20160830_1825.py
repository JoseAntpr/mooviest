# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20160829_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='original_title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie_lang',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
