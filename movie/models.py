import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Lang(models.Model):
    code = models.CharField(max_length=20,null=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Country(models.Model):
    name = models.CharField(max_length=20)
    lang = models.ForeignKey(Lang, null=True, on_delete=models.SET_NULL)
    def __str__(self):              # __unicode__ on Python 2
        return self.award

class Celebrity(models.Model):
    name = models.CharField(max_length=50)
    born = models.DateField('Born')
    image = models.CharField(max_length=255,null=True)
    twitter_account = models.CharField(max_length=30)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Celebrity_lang(models.Model):
    biography = models.CharField(max_length=600)
    address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=30)
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.biography

class Role(models.Model):
    code = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Role_lang(models.Model):
    name = models.CharField(max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Saga(models.Model):
    code = models.CharField(max_length=20,null=False,default='s')
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Saga_lang(models.Model):
    name = models.CharField(max_length=30)
    synopsis = models.CharField(max_length=800)
    saga = models.ForeignKey(Saga, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Genre(models.Model):
    code = models.CharField(max_length=20,null=False,default='g')
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Genre_lang(models.Model):
    name = models.CharField(max_length=20)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Emotion(models.Model):
    code = models.CharField(max_length=20,null=False,default='e')
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Emotion_lang(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Movie(models.Model):
    image = models.CharField(max_length=255,null=True)
    runtime = models.PositiveSmallIntegerField(null=True)
    movie_producer = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    synopsis = models.TextField(max_length=800)
    duration = models.DurationField('Duration')
    released = models.PositiveSmallIntegerField(null=True)
    country = models.CharField(max_length=30)
    saga_order = models.IntegerField(default=1,blank=True)
    average = models.DecimalField(default=0, max_digits=4, decimal_places=2, null=True, blank=True)
    participations = models.ManyToManyField(Celebrity, through =
    'Participation')
    saga = models.ForeignKey(Saga,null=True,blank=True,on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    emotions = models.ManyToManyField(Emotion,blank=True)
    ratings = models.ManyToManyField(Source,blank=True,through = 'Rating')

    def __str__(self):              # __unicode__ on Python 2
        return self.duration


class Rating(models.Model):
    source = models.ForeignKey(Source, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    sourceid = models.CharField(max_length=30)
    rating = models.PositiveSmallIntegerField(default=0,null=True)
    count = models.PositiveSmallIntegerField(null=True,default=0)

class Movie_lang(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=800)
    country = models.ForeignKey(Country, null= True, on_delete=models.SET_NULL)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

class Participation(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete = models.SET_NULL)
    def __str__(self):              # __unicode__ on Python 2
        return self.role
    class Meta:
        unique_together = (("celebrity", "movie","role"),)

class Participation_lang(models.Model):
    award = models.CharField(max_length=200)
    participation = models.ForeignKey(Participation, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.award

class Streaming(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Catalogue(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    streaming = models.ForeignKey(Streaming, on_delete = models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.streaming.name
    class Meta:
        unique_together = (("movie", "streaming"),)

class Catalogue_lang(models.Model):
    url = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2, null=True, blank=True)
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    def __str__(self):              # __unicode__ on Python 2
        return self.award
