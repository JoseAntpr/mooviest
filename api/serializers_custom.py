from rest_framework import serializers
from movie.models import Movie, Movie_lang, Rating, Country, Genre, Genre_lang, Celebrity, Participation, Celebrity_lang

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
        fields = ('country', 'title', 'synopsis','image','trailer')

class Genre_LangAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre_lang
        fields = ("name")

class GenreAppSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        lang = self.context['lang']
        genre_lang = Genre_lang.objects.get(lang = lang, genre = obj)
        return genre_lang.name


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

class MovieListCustomSerializer(serializers.BaseSerializer):
    def to_representation(self,obj):

        return {
            'id': obj.movie.id,
            'average': obj.movie.average,
            'image': obj.image,
            'title': obj.title,
            'movie_lang_id': obj.id
        }

class MovieAppSerializer(serializers.ModelSerializer):
    ratings = RatingAppSerializer(source='rating_set', many=True)
    genres = GenreAppSerializer(many=True)
    langs = serializers.SerializerMethodField('get')
    participations = serializers.SerializerMethodField('get_participation')

    def get(self, obj):
        lang = self.context['lang']
        langs = Movie_lang.objects.get(lang = lang, movie = obj)
        langSerializer = Movie_LangAppSerializer( instance = langs)
        return langSerializer.data

    def get_participation(self, obj):
        lang = self.context['lang']
        participations = Participation.objects.filter(movie = obj)
        participationSerializer = ParticipationAppSerializer(source='participation_set', many=True, instance = participations)
        return participationSerializer.data

    class Meta:
        model = Movie
        fields = ('id', 'genres', 'participations', 'langs', 'emotions', 'ratings', 'original_title', 'runtime', 'released', 'movie_producer', 'saga_order', 'average')
