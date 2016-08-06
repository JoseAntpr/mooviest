# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20160714_1951'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMovie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('born', models.DateField()),
                ('gender', models.CharField(max_length=6, choices=[('FE', 'Female'), ('MA', 'Male')])),
                ('photo_profile', models.ImageField(null=True, default='user/profile/no-image.png', upload_to='user/profile')),
                ('cover_page', models.ImageField(null=True, default='user/cover/no-image.png', upload_to='user/cover')),
                ('city', models.CharField(max_length=35)),
                ('country', models.ForeignKey(to='movie.Country')),
                ('followers', models.ManyToManyField(to='users.UserProfile')),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('movies', models.ManyToManyField(through='users.Collection', to='movie.Movie')),
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
    ]
