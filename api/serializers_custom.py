from rest_framework import serializers
from movie.models import Movie, Movie_lang, Rating, Country

class CountryAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'lang', 'name', 'code')

class RatingAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'name', 'rating', 'count', 'date_update')

class Movie_LangAppSerializer(serializers.ModelSerializer):
    country = CountryAppSerializer()
    class Meta:
        model = Movie_lang
        fields = ('id', 'movie', 'lang', 'country', 'title', 'synopsis','image','trailer')

class MovieAppSerializer(serializers.ModelSerializer):
    langs = Movie_LangAppSerializer(source='movie_lang_set', many=True)
    ratings = RatingAppSerializer(source='rating_set', many=True)
    class Meta:
        model = Movie
        fields = ('id', 'genres', 'participations', 'langs', 'emotions', 'ratings', 'original_title', 'runtime', 'released', 'movie_producer', 'saga_order', 'average')
