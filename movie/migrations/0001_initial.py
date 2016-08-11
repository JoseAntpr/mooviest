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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=4, blank=True, null=True, decimal_places=2, default=0)),
                ('catalogue', models.ForeignKey(to='movie.Catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('born', models.DateField(blank=True, null=True, verbose_name='Born')),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_account', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('biography', models.TextField(blank=True, max_length=600, null=True)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=10, default='US')),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=20, default='e')),
            ],
        ),
        migrations.CreateModel(
            name='Emotion_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('emotion', models.ForeignKey(to='movie.Emotion')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=20, default='g')),
            ],
        ),
        migrations.CreateModel(
            name='Genre_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('genre', models.ForeignKey(to='movie.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('original_title', models.CharField(max_length=100)),
                ('runtime', models.PositiveSmallIntegerField(null=True)),
                ('released', models.PositiveSmallIntegerField(null=True)),
                ('movie_producer', models.CharField(max_length=255)),
                ('saga_order', models.IntegerField(blank=True, default=1)),
                ('average', models.DecimalField(max_digits=4, blank=True, null=True, decimal_places=2, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('synopsis', models.TextField(max_length=800)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('trailer', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Country')),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('character', models.CharField(blank=True, max_length=100, null=True)),
                ('award', models.CharField(blank=True, max_length=200, null=True)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sourceid', models.CharField(max_length=30)),
                ('rating', models.PositiveSmallIntegerField(null=True, default=0)),
                ('count', models.IntegerField(null=True, default=0)),
                ('date_update', models.DateField(auto_now=True, null=True)),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('role', models.ForeignKey(to='movie.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Saga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(max_length=20, default='s')),
            ],
        ),
        migrations.CreateModel(
            name='Saga_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('synopsis', models.CharField(blank=True, max_length=800, null=True)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('saga', models.ForeignKey(to='movie.Saga')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Streaming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='saga',
            name='langs',
            field=models.ManyToManyField(through='movie.Saga_lang', to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='role',
            name='langs',
            field=models.ManyToManyField(through='movie.Role_lang', to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='rating',
            name='source',
            field=models.ForeignKey(to='movie.Source'),
        ),
        migrations.AddField(
            model_name='participation',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Role'),
        ),
        migrations.AddField(
            model_name='movie',
            name='catalogues',
            field=models.ManyToManyField(through='movie.Catalogue', to='movie.Streaming'),
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
            field=models.ManyToManyField(through='movie.Movie_lang', to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='movie',
            name='participations',
            field=models.ManyToManyField(through='movie.Participation', to='movie.Celebrity'),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.ManyToManyField(blank=True, through='movie.Rating', to='movie.Source'),
        ),
        migrations.AddField(
            model_name='movie',
            name='saga',
            field=models.ForeignKey(blank=True, null=True, to='movie.Saga'),
        ),
        migrations.AddField(
            model_name='genre_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='genre',
            name='langs',
            field=models.ManyToManyField(through='movie.Genre_lang', to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='emotion_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='emotion',
            name='langs',
            field=models.ManyToManyField(through='movie.Emotion_lang', to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='country',
            name='lang',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='celebrity_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='celebrity',
            name='langs',
            field=models.ManyToManyField(through='movie.Celebrity_lang', to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='catalogue_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='catalogue',
            name='langs',
            field=models.ManyToManyField(through='movie.Catalogue_lang', to='movie.Lang'),
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
