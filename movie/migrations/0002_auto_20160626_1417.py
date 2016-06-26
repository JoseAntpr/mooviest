# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='released',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='average',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, default=0, max_digits=4),
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
            field=models.ForeignKey(null=True, to='movie.Saga'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='saga_order',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(max_length=800),
        ),
    ]
