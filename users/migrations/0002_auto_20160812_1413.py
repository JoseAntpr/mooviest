# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20160812_1413'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pub_date', models.DateTimeField(null=True, auto_now_add=True)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
                ('profile', models.ForeignKey(to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(to='movie.Celebrity', through='users.Follower'),
        ),
    ]
