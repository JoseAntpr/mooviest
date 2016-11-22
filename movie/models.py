"""Mooviest models module.
This module defines the main models used in the application

"""
from django.db import models


class Lang(models.Model):
    """
    A `Lang` represents an idiom that the user can select
    while using the application. Determines how should be translated other
    models like a `Country`, a `Celebrity`or a `Movie`.

    Attributes:
        code: The code that identifies the language. Examples: 'en, 'es'
    """
    code = models.CharField(max_length=20, null=False)


    def __str__(self):
        return self.code


class Country(models.Model):
    """
    Represents a country that is related to `Profile` and a `Movie`.

    Attributes:
        language: The `Language` in which the `name` is expressed
        name: The name of the `Country` object
        code: The character sequence that identifies the object. Examples: 'US', 'XX'
    """
    lang = models.ForeignKey(Lang, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=20, null=False)
    code = models.CharField(max_length=10, null=False, default='US')


    def __str__(self):
        return self.name


class Celebrity(models.Model):
    """
    A `Celebrity` is a person related to a movie, like an actor/actress,
    the director or writer.

    Attributes:
        langs: The profiles of the celebrity in other languages
        name: The name of the celebrity
        born: The born date
        image: A profile image fo the celebrity
    """
    langs = models.ManyToManyField(Lang, through='Celebrity_lang')
    name = models.CharField(max_length=250)
    born = models.DateField('Born', null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    twitter_account = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name


class Celebrity_lang(models.Model):
    """
    This class is used to represent some information about a `Celebrity`
    in other languages.

    Attributes:
        celebrity: The `Celebrity` instance which represents
        lang: The language in which the information is presented
    """
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    biography = models.TextField(max_length=10000, blank=True, null=True)


    def __str__(self):
        return self.celebrity + " " + self.lang


class Role(models.Model):
    """
    A `Role` is a title that has a person related to a movie.
    Examples: actor, director, producer.

    Attributes:
        langs: The name of the role in other languages
        code: The name of the role
    """
    langs = models.ManyToManyField(Lang, through='Role_lang')
    code = models.CharField(max_length=20)


    def __str__(self):
        return self.code


class Role_lang(models.Model):
    """
    This class is used to represent a `Role` in other languages.

    Attributes:
        role: The `Role` instance which represents
        lang: The language in which the role is presented
        name: The translated name of the role.
    """
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Saga(models.Model):
    """
    A `Saga` a simple collection of movies that belongs to a
    same movie series.

    Attributes:
        langs: The saga in other languages
        code: The name of the saga
    """
    langs = models.ManyToManyField(Lang, through='Saga_lang')
    code = models.CharField(max_length=20, null=False, default='s')


    def __str__(self):
        return self.code


class Saga_lang(models.Model):
    """
    This class represents a `Saga` in other languages.

    Attributes:
        saga: The `Saga` instance which represents
        lang: The language in which the saga is presented
    """
    saga = models.ForeignKey(Saga, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    synopsis = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    A `Genre`is a motion picture category based on narrative or
    technical similarities.

    Attributes:
        langs: The genre in other languages
        code: The name of the genre
    """
    langs = models.ManyToManyField(Lang, through='Genre_lang')
    code = models.CharField(max_length=20, null=False, default='g')


    def __str__(self):  # __unicode__ on Python 2
        return self.code


class Genre_lang(models.Model):
    """
    This class represents a `Genre` in other languages.

    Attributes:
        genre: The `Genre` instance which represents
        lang: The language in which the genre is presented
    """
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Emotion(models.Model):
    """
    An emotion is a personal state that the user can relate to a movie.

    Attributes:
        langs: The `Emotion` in other languages
        code: The name of the emotion
    """
    langs = models.ManyToManyField(Lang, through='Emotion_lang')
    code = models.CharField(max_length=20, null=False, default='e')


    def __str__(self):
        return self.code


class Emotion_lang(models.Model):
    """
    This class represents an `Emotion` in other languages.

    Attributes:
        emotion: The `Emotion` instance which represents.
        lang: The language in which the emotion is presented
    """
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.name


class Streaming(models.Model):
    # TODO: Write the docstring documentation of this class
    """
    This class represents ?

    Attributes:
        name:
        url:
    """
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name


class Source(models.Model):
    # TODO: Write the docstring documentation of this class
    """
    This class represents ?

    """
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    A `Movie`is an audiovisual creation where actors, producers and other
    `Celebrities' are involved. An user can relate emotions to a movie as well as a rating.

    """
    genres = models.ManyToManyField(Genre, blank=True)
    participations = models.ManyToManyField(Celebrity, through=
    'Participation')
    langs = models.ManyToManyField(Lang, through='Movie_lang')
    emotions = models.ManyToManyField(Emotion, blank=True)
    saga = models.ForeignKey(Saga, null=True, blank=True, on_delete=models.CASCADE)
    catalogues = models.ManyToManyField(Streaming, through='Catalogue')
    ratings = models.ManyToManyField(Source, blank=True, through='Rating')
    original_title = models.CharField(max_length=255)
    runtime = models.PositiveSmallIntegerField(null=True)
    released = models.PositiveSmallIntegerField(null=True)
    backdrop = models.CharField(max_length=255, null=True, blank=True)
    movie_producer = models.TextField(null=True, blank=True)
    saga_order = models.IntegerField(default=1, blank=True)
    average = models.DecimalField(default=0, max_digits=4, decimal_places=2, null=True, blank=True)


    def __str__(self):
        return self.original_title


    def get_movie_lang(self, lang):
        return Movie_lang.objects.filter(lang__code=lang).select_related('movie').get(movie=self)


class Movie_lang(models.Model):
    """
    This class represents a `Movie` in other languages.

    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_lang")
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE, related_name="movie_lang")
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    trailer = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.title


class Rating(models.Model):
    """
    A `Rating`is a measure that can be applied to a `Movie` or a `Source`.

    """
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    sourceid = models.CharField(max_length=200)
    name = models.CharField(max_length=30, null=True)
    rating = models.PositiveSmallIntegerField(default=0, null=True)
    count = models.IntegerField(null=True, default=0)
    date_update = models.DateField(auto_now=True, null=True)


class Catalogue(models.Model):
    # TODO: Write the docstring documentation of this class
    """
    A `Catalogue` is ?

    Attributes:
        movie:
        streaming:
        langs: The catalogue in other languages
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    streaming = models.ForeignKey(Streaming, on_delete=models.CASCADE)
    langs = models.ManyToManyField(Lang, through='Catalogue_lang')

    # def __str__(self):              # __unicode__ on Python 2
    #    return self.streaming
    class Meta:
        unique_together = (("movie", "streaming"),)


class Catalogue_lang(models.Model):
    """
    This class is used to represent a `Catalogue` in other languages.

    """
    catalogue = models.ForeignKey(Catalogue, on_delete=models.CASCADE)
    lang = models.ForeignKey(Lang, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2, null=True, blank=True)
    # def __str__(self):              # __unicode__ on Python 2
    #    return self.catalogue + " " + self.lang


class Participation(models.Model):
    """
    A `Participation` defines the inclusion of a `Celebrity` in a `Movie`

    Attributes:
        celebrity: The `Celebrity` instance whom the participation is related.
        movie: The `Movie` instance in which the celebrity is related.
        role: The `Role`of the celebrity in the movie.
        character: The film character that is permormed by the celebrity.
    """
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    character = models.TextField(blank=True, null=True)
    award = models.CharField(max_length=200, blank=True, null=True)

    # def __str__(self):              # __unicode__ on Python 2
    #    return self.character
    class Meta:
        unique_together = (("celebrity", "movie", "role"),)
