# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity_lang',
            name='biography',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
