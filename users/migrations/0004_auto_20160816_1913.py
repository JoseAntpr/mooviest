# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160816_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lang',
            field=models.ForeignKey(null=True, blank=True, to='movie.Lang'),
        ),
    ]
