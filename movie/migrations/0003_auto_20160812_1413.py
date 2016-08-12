# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20160811_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='name',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='rating',
            name='sourceid',
            field=models.CharField(max_length=200),
        ),
    ]
