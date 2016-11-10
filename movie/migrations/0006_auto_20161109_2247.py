# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_backdrop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='lang',
            new_name='language',
        ),
    ]
