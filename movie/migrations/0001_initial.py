# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue_lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('url', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, null=True, default=0, max_digits=4, blank=True)),
                ('catalogue', models.ForeignKey(to='movie.Catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('born', models.DateField(verbose_name='Born')),
                ('image', models.CharField(null=True, max_length=255, blank=True)),
                ('twitter_account', models.CharField(null=True, max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity_lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('biography', models.TextField(max_length=600)),
                ('address', models.CharField(null=True, max_length=100, blank=True)),
                ('nationality', models.CharField(null=True, max_length=30, blank=True)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=10, default='US')),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=20, default='e')),
            ],
        ),
        migrations.CreateModel(
            name='Emotion_lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('emotion', models.ForeignKey(to='movie.Emotion')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=20, default='g')),
            ],
        ),
        migrations.CreateModel(
            name='Genre_lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('genre', models.ForeignKey(to='movie.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('original_title', models.CharField(max_length=100)),
                ('runtime', models.PositiveSmallIntegerField(null=True)),
                ('released', models.PositiveSmallIntegerField(null=True)),
                ('image', models.CharField(null=True, max_length=255, blank=True)),
                ('movie_producer', models.CharField(max_length=255)),
                ('saga_order', models.IntegerField(blank=True, default=1)),
                ('average', models.DecimalField(decimal_places=2, null=True, default=0, max_digits=4, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('synopsis', models.TextField(max_length=800)),
                ('country', models.ForeignKey(to='movie.Country', on_delete=django.db.models.deletion.SET_NULL, null=True)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('character', models.CharField(max_length=100, default='')),
                ('award', models.CharField(null=True, max_length=200, blank=True)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('sourceid', models.CharField(max_length=30)),
                ('rating', models.PositiveSmallIntegerField(null=True, default=0)),
                ('count', models.IntegerField(null=True, default=0)),
                ('date_update', models.DateField(null=True, auto_now=True)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role_lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('role', models.ForeignKey(to='movie.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Saga',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=20, default='s')),
            ],
        ),
        migrations.CreateModel(
            name='Saga_lang',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('synopsis', models.CharField(max_length=800)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('saga', models.ForeignKey(to='movie.Saga')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Streaming',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='saga',
            name='langs',
            field=models.ManyToManyField(to='movie.Lang', through='movie.Saga_lang'),
        ),
        migrations.AddField(
            model_name='role',
            name='langs',
            field=models.ManyToManyField(to='movie.Lang', through='movie.Role_lang'),
        ),
        migrations.AddField(
            model_name='rating',
            name='source',
            field=models.ForeignKey(to='movie.Source'),
        ),
        migrations.AddField(
            model_name='participation',
            name='role',
            field=models.ForeignKey(to='movie.Role', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='catalogues',
            field=models.ManyToManyField(to='movie.Streaming', through='movie.Catalogue'),
        ),
        migrations.AddField(
            model_name='movie',
            name='emotions',
            field=models.ManyToManyField(blank=True, to='movie.Emotion'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movie.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='langs',
            field=models.ManyToManyField(to='movie.Lang', through='movie.Movie_lang'),
        ),
        migrations.AddField(
            model_name='movie',
            name='participations',
            field=models.ManyToManyField(to='movie.Celebrity', through='movie.Participation'),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.ManyToManyField(blank=True, to='movie.Source', through='movie.Rating'),
        ),
        migrations.AddField(
            model_name='movie',
            name='saga',
            field=models.ForeignKey(to='movie.Saga', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='genre_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='genre',
            name='langs',
            field=models.ManyToManyField(to='movie.Lang', through='movie.Genre_lang'),
        ),
        migrations.AddField(
            model_name='emotion_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='emotion',
            name='langs',
            field=models.ManyToManyField(to='movie.Lang', through='movie.Emotion_lang'),
        ),
        migrations.AddField(
            model_name='country',
            name='lang',
            field=models.ForeignKey(to='movie.Lang', on_delete=django.db.models.deletion.SET_NULL, null=True),
        ),
        migrations.AddField(
            model_name='celebrity_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='celebrity',
            name='langs',
            field=models.ManyToManyField(to='movie.Lang', through='movie.Celebrity_lang'),
        ),
        migrations.AddField(
            model_name='catalogue_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='langs',
            field=models.ManyToManyField(to='movie.Lang', through='movie.Catalogue_lang'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='movie',
            field=models.ForeignKey(to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='streaming',
            field=models.ForeignKey(to='movie.Streaming'),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('celebrity', 'movie', 'role')]),
        ),
        migrations.AlterUniqueTogether(
            name='catalogue',
            unique_together=set([('movie', 'streaming')]),
        ),
    ]
