# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160902_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.ImageField(blank=True, null=True, default='user/no-image.png', upload_to='user_directory_path_profile'),
        ),
    ]
