from rest_framework import serializers
from movie.models import Movie, Movie_lang, Rating, Country, Genre, Genre_lang, Celebrity, Participation, Celebrity_lang

class CountryAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'code')

class RatingAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('name', 'rating', 'count', 'date_update', "sourceid")

class Movie_LangAppSerializer(serializers.ModelSerializer):
    country = CountryAppSerializer()
    class Meta:
        model = Movie_lang
        fields = ('id','country', 'title', 'synopsis','image','trailer')

class Genre_LangAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre_lang
        fields = ('name',)

class GenreAppSerializer(serializers.ModelSerializer):
    langs = serializers.SerializerMethodField('get')
    def get(self, obj):
        lang = self.context['lang']
        langs = Genre_lang.objects.filter(lang = lang, genre = obj)
        langSerializer = Genre_LangAppSerializer(source='genre_lang_set', many=True, instance = langs)
        return langSerializer.data
    class Meta:
        model = Genre
        fields = ('langs',)

class Celebrity_langAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity_lang
        fields = ('id', 'celebrity', 'lang', 'biography')

class CelebrityAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ('id', 'name', 'born', 'image', 'twitter_account', 'address')

class ParticipationAppSerializer(serializers.ModelSerializer):
    celebrity = CelebrityAppSerializer(many= False)
    class Meta:
        model = Participation
        fields = ('celebrity', 'role', 'character', 'award')

class MovieAppSerializer(serializers.ModelSerializer):
    ratings = serializers.SerializerMethodField('get_rating')
    genres = GenreAppSerializer(many=True)
    langs = serializers.SerializerMethodField('get')
    participations = serializers.SerializerMethodField('get_participation')

    def get(self, obj):
        lang = self.context['lang']
        langs = Movie_lang.objects.filter(lang = lang, movie = obj)
        langSerializer = Movie_LangAppSerializer(source='movie_lang_set', many=True, instance = langs)
        return langSerializer.data

    def get_participation(self, obj):
        lang = self.context['lang']
        participations = Participation.objects.filter(movie = obj)
        participationSerializer = ParticipationAppSerializer(source='participation_set', many=True, instance = participations)
        return participationSerializer.data
    def get_rating(self,obj):
        ratings = Rating.objects.filter(movie = obj, name = "Tviso")
        ratingSerializer = RatingAppSerializer(source ="rating_set", many = True, instance = ratings)
        return ratingSerializer.data

    class Meta:
        model = Movie
        fields = ('id', 'genres', 'participations', 'langs', 'emotions', 'ratings', 'original_title', 'runtime', 'released', 'backdrop', 'movie_producer', 'saga_order', 'average')
