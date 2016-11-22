# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20161109_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='language',
            new_name='lang',
        ),
    ]
