# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20160629_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='movie.Lang', null=True),
        ),
        migrations.AlterField(
            model_name='movie_lang',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='movie.Country', null=True),
        ),
        migrations.AlterField(
            model_name='participation',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='movie.Role', null=True),
        ),
    ]
