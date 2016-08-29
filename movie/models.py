import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Lang(models.Model):
    code = models.CharField(max_length=20,null=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Country(models.Model):
    lang = models.ForeignKey(Lang, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=20,null=False)
    code = models.CharField(max_length=10,null=False,default='US')
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Celebrity(models.Model):
    langs = models.ManyToManyField(Lang, through = 'Celebrity_lang')
    name = models.CharField(max_length=255)
    born = models.DateField('Born',null=True,blank=True)
    image = models.CharField(max_length=255,null=True,blank=True)
    twitter_account = models.CharField(max_length=30,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Celebrity_lang(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    biography = models.TextField(max_length=10000,blank=True,null=True)
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.celebrity + " " + self.lang

class Role(models.Model):
    langs = models.ManyToManyField(Lang, through = 'Role_lang')
    code = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Role_lang(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Saga(models.Model):
    langs = models.ManyToManyField(Lang, through = 'Saga_lang')
    code = models.CharField(max_length=20,null=False,default='s')
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Saga_lang(models.Model):
    saga = models.ForeignKey(Saga, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    synopsis = models.TextField(blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Genre(models.Model):
    langs = models.ManyToManyField(Lang, through = 'Genre_lang')
    code = models.CharField(max_length=20,null=False,default='g')
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Genre_lang(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Emotion(models.Model):
    langs = models.ManyToManyField(Lang, through = 'Emotion_lang')
    code = models.CharField(max_length=20,null=False,default='e')
    def __str__(self):              # __unicode__ on Python 2
        return self.code

class Emotion_lang(models.Model):
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Streaming(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Movie(models.Model):
    genres = models.ManyToManyField(Genre,blank = True)
    participations = models.ManyToManyField(Celebrity, through =
    'Participation')
    langs = models.ManyToManyField(Lang, through = 'Movie_lang')
    emotions = models.ManyToManyField(Emotion,blank = True)
    saga = models.ForeignKey(Saga,null = True,blank = True,on_delete = models.CASCADE)
    catalogues = models.ManyToManyField(Streaming, through = 'Catalogue')
    ratings = models.ManyToManyField(Source,blank = True,through = 'Rating')
    original_title = models.CharField(max_length = 255)
    runtime = models.PositiveSmallIntegerField(null = True)
    released = models.PositiveSmallIntegerField(null = True)
    movie_producer = models.TextField(null=True,blank = True)
    saga_order = models.IntegerField(default = 1,blank = True)
    average = models.DecimalField(default = 0, max_digits = 4, decimal_places = 2, null = True, blank = True)
    def __str__(self):              # __unicode__ on Python 2
        return self.original_title

class Movie_lang(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null= True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True,null=True)
    image = models.CharField(max_length = 255,null = True,blank = True)
    trailer = models.CharField(max_length = 255,null = True,blank = True)
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.title

class Rating(models.Model):
    source = models.ForeignKey(Source, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    sourceid = models.CharField(max_length = 200)
    name = models.CharField(max_length = 30,null= True)
    rating = models.PositiveSmallIntegerField(default = 0,null = True)
    count = models.IntegerField(null = True,default = 0)
    date_update = models.DateField(auto_now = True, null= True)

class Catalogue(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    streaming = models.ForeignKey(Streaming, on_delete = models.CASCADE)
    langs = models.ManyToManyField(Lang, through = 'Catalogue_lang')
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.streaming
    class Meta:
        unique_together = (("movie", "streaming"),)

class Catalogue_lang(models.Model):
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2, null=True, blank=True)
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.catalogue + " " + self.lang

class Participation(models.Model):
    celebrity = models.ForeignKey(Celebrity, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete = models.SET_NULL)
    character = models.TextField(blank=True,null=True)
    award = models.CharField(max_length=200,blank=True,null=True)
    #def __str__(self):              # __unicode__ on Python 2
    #    return self.character
    class Meta:
        unique_together = (("celebrity", "movie","role"),)
