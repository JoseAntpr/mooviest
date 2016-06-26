# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('biography', models.CharField(max_length=600)),
                ('born', models.DateField(verbose_name='Born')),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=30)),
                ('twitter_account', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('synopsis', models.CharField(max_length=800)),
                ('duration', models.TimeField(verbose_name='Duration')),
                ('date', models.DateField(verbose_name='Date')),
                ('country', models.CharField(max_length=30)),
                ('movie_producer', models.CharField(max_length=100)),
                ('saga_order', models.IntegerField(default=1)),
                ('average', models.FloatField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('emotions', models.ManyToManyField(to='movie.Emotion')),
                ('genres', models.ManyToManyField(to='movie.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award', models.CharField(max_length=200)),
                ('celebrity', models.ForeignKey(to='movie.Celebrity')),
                ('movie', models.ForeignKey(to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Saga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('synopsis', models.CharField(max_length=800)),
            ],
        ),
        migrations.AddField(
            model_name='participation',
            name='role',
            field=models.ForeignKey(to='movie.Role'),
        ),
        migrations.AddField(
            model_name='movie',
            name='participations',
            field=models.ManyToManyField(through='movie.Participation', to='movie.Celebrity'),
        ),
        migrations.AddField(
            model_name='movie',
            name='saga',
            field=models.ForeignKey(to='movie.Saga'),
        ),
    ]
