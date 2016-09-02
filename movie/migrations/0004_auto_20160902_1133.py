# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20160830_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_lang',
            name='lang',
            field=models.ForeignKey(related_name='movie_lang', to='movie.Lang'),
        ),
        migrations.AlterField(
            model_name='movie_lang',
            name='movie',
            field=models.ForeignKey(related_name='movie_lang', to='movie.Movie'),
        ),
    ]
