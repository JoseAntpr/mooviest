# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160902_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_page',
            field=models.ImageField(null=True, blank=True, upload_to=users.models.user_directory_path_profile, default='user/no-image.png'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.ImageField(null=True, blank=True, upload_to=users.models.user_directory_path_profile, default='user/default/no-image.png'),
        ),
    ]
