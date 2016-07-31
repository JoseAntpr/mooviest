# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celebrity',
            name='image',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='celebrity',
            name='twitter_account',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='celebrity_lang',
            name='address',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='celebrity_lang',
            name='biography',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='celebrity_lang',
            name='nationality',
            field=models.CharField(null=True, max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(null=True, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='movie_lang',
            name='synopsis',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='participation',
            name='award',
            field=models.CharField(null=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
