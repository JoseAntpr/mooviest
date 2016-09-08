# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160906_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='photo_profile',
            new_name='avatar',
        ),
    ]
