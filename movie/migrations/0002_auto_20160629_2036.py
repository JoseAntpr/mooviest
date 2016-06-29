# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Catalogue_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True, default=0)),
                ('catalogue', models.ForeignKey(to='movie.Catalogue')),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('biography', models.CharField(max_length=600)),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Emotion_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('synopsis', models.CharField(max_length=800)),
                ('country', models.ForeignKey(to='movie.Country')),
                ('lang', models.ForeignKey(to='movie.Lang')),
            ],
        ),
        migrations.CreateModel(
            name='Participation_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('award', models.CharField(max_length=200)),
                ('lang', models.ForeignKey(to='movie.Lang')),
            ],
        ),
        migrations.CreateModel(
            name='Role_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lang', models.ForeignKey(to='movie.Lang')),
            ],
        ),
        migrations.CreateModel(
            name='Saga_lang',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('synopsis', models.CharField(max_length=800)),
                ('lang', models.ForeignKey(to='movie.Lang')),
            ],
        ),
        migrations.CreateModel(
            name='Streaming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='role',
            old_name='name',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='celebrity',
            name='address',
        ),
        migrations.RemoveField(
            model_name='celebrity',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='celebrity',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='emotion',
            name='description',
        ),
        migrations.RemoveField(
            model_name='emotion',
            name='name',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='synopsis',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='title',
        ),
        migrations.RemoveField(
            model_name='saga',
            name='name',
        ),
        migrations.RemoveField(
            model_name='saga',
            name='synopsis',
        ),
        migrations.AddField(
            model_name='celebrity',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='emotion',
            name='code',
            field=models.CharField(max_length=20, default='e'),
        ),
        migrations.AddField(
            model_name='genre',
            name='code',
            field=models.CharField(max_length=20, default='g'),
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='released',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='saga',
            name='code',
            field=models.CharField(max_length=20, default='s'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='average',
            field=models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True, default=0),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(verbose_name='Duration'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='emotions',
            field=models.ManyToManyField(blank=True, to='movie.Emotion'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='saga',
            field=models.ForeignKey(to='movie.Saga', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='saga_order',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set([('celebrity', 'movie', 'role')]),
        ),
        migrations.AddField(
            model_name='saga_lang',
            name='saga',
            field=models.ForeignKey(to='movie.Saga'),
        ),
        migrations.AddField(
            model_name='role_lang',
            name='role',
            field=models.ForeignKey(to='movie.Role'),
        ),
        migrations.AddField(
            model_name='participation_lang',
            name='participation',
            field=models.ForeignKey(to='movie.Participation'),
        ),
        migrations.AddField(
            model_name='movie_lang',
            name='movie',
            field=models.ForeignKey(to='movie.Movie'),
        ),
        migrations.AddField(
            model_name='genre_lang',
            name='genre',
            field=models.ForeignKey(to='movie.Genre'),
        ),
        migrations.AddField(
            model_name='genre_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='emotion_lang',
            name='emotion',
            field=models.ForeignKey(to='movie.Emotion'),
        ),
        migrations.AddField(
            model_name='emotion_lang',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='country',
            name='lang',
            field=models.ForeignKey(to='movie.Lang'),
        ),
        migrations.AddField(
            model_name='celebrity_lang',
            name='celebrity',
            field=models.ForeignKey(to='movie.Celebrity'),
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
        migrations.RemoveField(
            model_name='participation',
            name='award',
        ),
        migrations.AlterUniqueTogether(
            name='catalogue',
            unique_together=set([('movie', 'streaming')]),
        ),
    ]
