# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160816_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='collections',
            field=models.ManyToManyField(through='users.Collection', to='movie.Movie', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='feelings',
            field=models.ManyToManyField(through='users.Feeling', to='movie.Emotion', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(through='users.Follower', to='movie.Celebrity', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lang',
            field=models.ForeignKey(blank=True, to='movie.Lang'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(related_name='related_to', to='users.Profile', blank=True, through='users.Relationship'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
