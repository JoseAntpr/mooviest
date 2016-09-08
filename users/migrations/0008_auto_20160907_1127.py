# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160907_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='user/default/no-image.png', blank=True, null=True, upload_to=users.models.user_directory_path_profile),
        ),
    ]
