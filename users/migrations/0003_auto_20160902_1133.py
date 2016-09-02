# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160831_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='movie',
            field=models.ForeignKey(related_name='collection', to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cover_page',
            field=models.ImageField(default='user/no-image.png', upload_to='user_directory_path_profile', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.ImageField(width_field=180, height_field=180, upload_to='user_directory_path_profile', blank=True, null=True, default='user/no-image.png'),
        ),
    ]
