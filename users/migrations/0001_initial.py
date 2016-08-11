# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pub_date', models.DateTimeField(auto_now=True, null=True)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('emotion', models.ForeignKey(to='movie.Emotion')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('born', models.DateField()),
                ('gender', models.CharField(max_length=6, choices=[('FE', 'Female'), ('MA', 'Male')])),
                ('photo_profile', models.ImageField(upload_to='user/profile', null=True, default='user/profile/no-image.png')),
                ('cover_page', models.ImageField(upload_to='user/cover', null=True, default='user/cover/no-image.png')),
                ('city', models.CharField(max_length=35)),
                ('collections', models.ManyToManyField(through='users.Collection', to='movie.Movie')),
                ('country', models.ForeignKey(to='movie.Country')),
                ('feelings', models.ManyToManyField(through='users.Feeling', to='movie.Emotion')),
                ('lang', models.ForeignKey(to='movie.Lang')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
                ('from_person', models.ForeignKey(to='users.Profile', related_name='from_people')),
                ('to_person', models.ForeignKey(to='users.Profile', related_name='to_people')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(to='users.Profile', through='users.Relationship', related_name='related_to'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
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
