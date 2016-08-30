# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('pub_date', models.DateTimeField(null=True, auto_now=True)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('emotion', models.ForeignKey(to='movie.Emotion')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='LikeCelebrity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('born', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(max_length=6, choices=[('FE', 'Female'), ('MA', 'Male')], null=True, blank=True)),
                ('photo_profile', models.ImageField(upload_to='user/profile/', default='user/profile/no-image.png', null=True, blank=True)),
                ('cover_page', models.ImageField(upload_to='user/cover', default='user/cover/no-image.png', null=True, blank=True)),
                ('city', models.CharField(max_length=35, null=True, blank=True)),
                ('postalCode', models.CharField(max_length=35, null=True, blank=True)),
                ('collections', models.ManyToManyField(to='movie.Movie', through='users.Collection', blank=True)),
                ('country', models.ForeignKey(to='movie.Country', blank=True, null=True)),
                ('feelings', models.ManyToManyField(to='movie.Emotion', through='users.Feeling', blank=True)),
                ('lang', models.ForeignKey(to='movie.Lang', blank=True, null=True)),
                ('likeCelebrities', models.ManyToManyField(to='movie.Celebrity', through='users.LikeCelebrity', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
                ('from_person', models.ForeignKey(to='users.Profile', related_name='from_people')),
                ('to_person', models.ForeignKey(to='users.Profile', related_name='to_people')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMovie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(to='users.Profile', related_name='related_to', through='users.Relationship', blank=True),
        ),
        migrations.AddField(
            model_name='likecelebrity',
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
