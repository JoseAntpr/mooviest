from rest_framework import serializers
from movie.models import Movie, Movie_lang, Rating, Country, Genre_lang

class CountryAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'code')

class RatingAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('name', 'rating', 'count', 'date_update')

class Movie_LangAppSerializer(serializers.ModelSerializer):
    country = CountryAppSerializer()
    class Meta:
        model = Movie_lang
        fields = ('id', 'lang', 'country', 'title', 'synopsis','image','trailer')

class Genre_LangAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre_lang
        fields = ('id', 'genre', 'lang', 'name')

class MovieAppSerializer(serializers.ModelSerializer):
    ratings = RatingAppSerializer(source='rating_set', many=True)
    genres = serializers.SerializerMethodField('get_genres')
    langs = serializers.SerializerMethodField('get')

    def get(self, obj):
        lang = self.context['lang']
        langs = Movie_lang.objects.filter(lang = lang, movie = obj)
        langSerializer = Movie_LangAppSerializer(source='movie_lang_set', many=True, instance = langs)
        return langSerializer.data

    def get_genres(self, obj):
        lang = self.context['lang']
        genres = Genre_lang.objects.filter(lang=lang, movie= obj)

    class Meta:
        model = Movie
        fields = ('id', 'genres', 'participations', 'langs', 'emotions', 'ratings', 'original_title', 'runtime', 'released', 'movie_producer', 'saga_order', 'average')
