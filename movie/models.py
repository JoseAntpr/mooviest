import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Celebrity(models.Model):
    name = models.CharField(max_length=50)
    biography = models.CharField(max_length=600)
    born = models.DateField('Born')
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=30)
    twitter_account = models.CharField(max_length=30)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Saga(models.Model):
    name = models.CharField(max_length=30)
    synopsis = models.CharField(max_length=800)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Emotion(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=800)
    duration = models.TimeField('Duration')
    date = models.DateField('Date')
    country = models.CharField(max_length=30)
    movie_producer = models.CharField(max_length=100)
    saga_order = models.IntegerField(default = 1)
    average = models.FloatField()
    participations = models.ManyToManyField(Celebrity, through =
    'Participation')
    saga = models.ForeignKey(Saga, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    emotions = models.ManyToManyField(Emotion)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.title
class Participation(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    award = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.award
