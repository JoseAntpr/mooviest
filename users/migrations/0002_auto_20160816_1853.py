# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='postalCode',
            field=models.CharField(blank=True, null=True, max_length=35),
        ),
        migrations.AlterField(
            model_name='profile',
            name='born',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='collections',
            field=models.ManyToManyField(blank=True, through='users.Collection', to='movie.Movie', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(blank=True, to='movie.Country', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cover_page',
            field=models.ImageField(upload_to='user/cover', blank=True, null=True, default='user/cover/no-image.png'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='feelings',
            field=models.ManyToManyField(blank=True, through='users.Feeling', to='movie.Emotion', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, through='users.Follower', to='movie.Celebrity', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lang',
            field=models.ForeignKey(blank=True, to='movie.Lang', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.ImageField(upload_to='user/profile', blank=True, null=True, default='user/profile/no-image.png'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(related_name='related_to', blank=True, through='users.Relationship', to='users.Profile', null=True),
        ),
    ]
