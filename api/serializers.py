"""
This module specifies the serializers used by the `Django Rest Framework`_
that determines the outgoing information of the models in the application
through the API.

.. _Django Rest Framework:
   http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

"""
from rest_framework import serializers
from movie.models import *


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lang
        fields = ('code',)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'lang', 'name', 'code')


class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ('id', 'langs', 'name', 'born', 'image', 'twitter_account', 'address')


class Celebrity_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity_lang
        fields = ('id', 'celebrity', 'lang', 'biography')


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'langs', 'code')


class Role_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_lang
        fields = ('id', 'role', 'lang', 'name')


class SagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saga
        fields = ('id', 'langs', 'code')


class Saga_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saga_lang
        fields = ('id', 'saga', 'lang', 'name', 'synopsis')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'langs', 'code')


class Genre_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre_lang
        fields = ('id', 'genre', 'lang', 'name')


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ('id', 'langs', 'code')


class Emotion_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion_lang
        fields = ('id', 'emotion', 'lang', 'name', 'description')


class StreamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streaming
        fields = ('id', 'name', 'url')


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
        'id', 'genres', 'participations', 'langs', 'emotions', 'saga', 'catalogues', 'ratings', 'original_title',
        'runtime', 'released', 'backdrop', 'movie_producer', 'saga_order', 'average')


class Movie_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_lang
        fields = ('id', 'movie', 'lang', 'country', 'title', 'synopsis', 'image', 'trailer')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'source', 'movie', 'sourceid', 'name', 'rating', 'count', 'date_update')


class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = ('id', 'movie', 'streaming', 'langs')


class Catalogue_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue_lang
        fields = ('id', 'catalogue', 'lang', 'url', 'price')


class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = ('id', 'celebrity', 'movie', 'role', 'character', 'award')
