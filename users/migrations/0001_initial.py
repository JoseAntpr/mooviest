# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(auto_now=True, null=True)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('emotion', models.ForeignKey(to='movie.Emotion')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('born', models.DateField(null=True, blank=True)),
                ('gender', models.CharField(null=True, choices=[('FE', 'Female'), ('MA', 'Male')], blank=True, max_length=6)),
                ('photo_profile', models.ImageField(upload_to='user/profile', null=True, blank=True, default='user/profile/no-image.png')),
                ('cover_page', models.ImageField(upload_to='user/cover', null=True, blank=True, default='user/cover/no-image.png')),
                ('city', models.CharField(null=True, blank=True, max_length=35)),
                ('postalCode', models.CharField(null=True, blank=True, max_length=35)),
                ('collections', models.ManyToManyField(blank=True, through='users.Collection', to='movie.Movie')),
                ('country', models.ForeignKey(blank=True, null=True, to='movie.Country')),
                ('feelings', models.ManyToManyField(blank=True, through='users.Feeling', to='movie.Emotion')),
                ('followers', models.ManyToManyField(blank=True, through='users.Follower', to='movie.Celebrity')),
                ('lang', models.ForeignKey(blank=True, null=True, to='movie.Lang')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('status', models.IntegerField(choices=[(1, 'Following'), (2, 'Blocked')])),
                ('from_person', models.ForeignKey(related_name='from_people', to='users.Profile')),
                ('to_person', models.ForeignKey(related_name='to_people', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='TypeMovie',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='relationships',
            field=models.ManyToManyField(related_name='related_to', blank=True, through='users.Relationship', to='users.Profile'),
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
