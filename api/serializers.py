from rest_framework import serializers
from movie.models import Lang, Country, Celebrity, Celebrity_lang, Role, Role_lang, Saga, Saga_lang, Genre, Genre_lang, Emotion, Emotion_lang, Streaming, Source, Movie, Movie_lang, Rating, Catalogue, Catalogue_lang, Participation


class LangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lang
        fields = ('id', 'code')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'lang', 'name')

class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ('id', 'name', 'born', 'image', 'twitter_account')

class Celebrity_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity_lang
        fields = ('id', 'celebrity', 'lang', 'biography', 'address', 'nationality')

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
        fields = ('id', 'genres', 'participations', 'langs', 'emotions', 'saga', 'catalogues', 'ratings', 'original_title', 'runtime', 'released', 'image', 'movie_producer', 'saga_order', 'average')

class Movie_langSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_lang
        fields = ('id', 'movie', 'lang', 'country', 'title', 'synopsis')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'source', 'movie', 'sourceid', 'rating', 'count')

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
