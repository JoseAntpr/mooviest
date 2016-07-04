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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=4, default=0)),
                ('catalogue', models.ForeignKey(to='movie.Catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('born', models.DateField(verbose_name='Born')),
                ('image', models.CharField(null=True, max_length=255)),
                ('twitter_account', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('biography', models.CharField(max_length=600)),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=30)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='e', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Emotion_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('emotion', models.ForeignKey(to='movie.Emotion')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='g', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genre_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('genre', models.ForeignKey(to='movie.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(null=True, max_length=255)),
                ('runtime', models.PositiveSmallIntegerField(null=True)),
                ('movie_producer', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('synopsis', models.TextField(max_length=800)),
                ('duration', models.DurationField(verbose_name='Duration')),
                ('released', models.PositiveSmallIntegerField(null=True)),
                ('country', models.CharField(max_length=30)),
                ('saga_order', models.IntegerField(blank=True, default=1)),
                ('average', models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=4, default=0)),
                ('emotions', models.ManyToManyField(blank=True, to='movie.Emotion')),
                ('genres', models.ManyToManyField(to='movie.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('synopsis', models.CharField(max_length=800)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='movie.Country', null=True)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Participation_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=200)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('participation', models.ForeignKey(to='movie.Participation')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Role_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('role', models.ForeignKey(to='movie.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Saga',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='s', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Saga_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('synopsis', models.CharField(max_length=800)),
                ('lang', models.ForeignKey(to='movie.Lang')),
                ('saga', models.ForeignKey(to='movie.Saga')),
            ],
        ),
        migrations.CreateModel(
            name='Streaming',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='participation',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='movie.Role', null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='participations',
            field=models.ManyToManyField(through='movie.Participation', to='movie.Celebrity'),
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
            model_name='emotion_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='country',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='movie.Lang', null=True),
        ),
        migrations.AddField(
            model_name='celebrity_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='catalogue_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
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
