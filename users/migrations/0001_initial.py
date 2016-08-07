# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('born', models.DateField()),
                ('gender', models.CharField(max_length=6, choices=[('FE', 'Female'), ('MA', 'Male')])),
                ('photo_profile', models.ImageField(upload_to='user/profile', default='user/profile/no-image.png', null=True)),
                ('cover_page', models.ImageField(upload_to='user/cover', default='user/cover/no-image.png', null=True)),
                ('city', models.CharField(max_length=35)),
                ('country', models.ForeignKey(to='movie.Country')),
                ('followers', models.ManyToManyField(to='users.UserProfile')),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('movies', models.ManyToManyField(to='movie.Movie', through='users.Collection')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='collection',
            name='typeMovie',
            field=models.ForeignKey(to='users.TypeMovie'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('movie', 'user')]),
        ),
    ]
