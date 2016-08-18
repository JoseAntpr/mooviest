# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0003_auto_20160812_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(auto_now=True, null=True)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('emotion', models.ForeignKey(to='movie.Emotion')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('born', models.DateField()),
                ('gender', models.CharField(max_length=6, choices=[('FE', 'Female'), ('MA', 'Male')])),
                ('photo_profile', models.ImageField(null=True, default='user/profile/no-image.png', upload_to='user/profile')),
                ('cover_page', models.ImageField(null=True, default='user/cover/no-image.png', upload_to='user/cover')),
                ('city', models.CharField(max_length=35)),
                ('collections', models.ManyToManyField(to='movie.Movie', through='users.Collection')),
                ('country', models.ForeignKey(to='movie.Country')),
                ('feelings', models.ManyToManyField(to='movie.Emotion', through='users.Feeling')),
                ('followers', models.ManyToManyField(to='movie.Celebrity', through='users.Follower')),
                ('lang', models.ForeignKey(to='movie.Lang')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
                ('from_person', models.ForeignKey(to='users.Profile', related_name='from_people')),
                ('to_person', models.ForeignKey(to='users.Profile', related_name='to_people')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(to='users.Profile', related_name='related_to', through='users.Relationship'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follower',
            name='profile',
            field=models.ForeignKey(to='users.Profile'),
        ),
        migrations.AddField(
            model_name='feeling',
            name='profile',
            field=models.ForeignKey(to='users.Profile'),
        ),
        migrations.AddField(
            model_name='collection',
            name='typeMovie',
            field=models.ForeignKey(to='users.TypeMovie'),
        ),
        migrations.AddField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(to='users.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together=set([('movie', 'user')]),
        ),
    ]
