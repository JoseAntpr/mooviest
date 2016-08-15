from movie.models import Lang, Country, Celebrity, Celebrity_lang, Role, Role_lang, Saga, Saga_lang, Genre, Genre_lang, Emotion, Emotion_lang, Streaming, Source, Movie, Movie_lang, Rating, Catalogue, Catalogue_lang, Participation
from .serializers import LangSerializer, CountrySerializer, CelebritySerializer, Celebrity_langSerializer, RoleSerializer, Role_langSerializer, SagaSerializer, Saga_langSerializer, GenreSerializer, Genre_langSerializer, EmotionSerializer, Emotion_langSerializer, StreamingSerializer, SourceSerializer, MovieSerializer, Movie_langSerializer, RatingSerializer, CatalogueSerializer, Catalogue_langSerializer, ParticipationSerializer
from rest_framework import viewsets, filters


class LangViewSet(viewsets.ModelViewSet):
    serializer_class = LangSerializer
    queryset = Lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class CelebrityViewSet(viewsets.ModelViewSet):
    serializer_class = CelebritySerializer
    queryset = Celebrity.objects.all()
    # Search for celebrity
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class Celebrity_langViewSet(viewsets.ModelViewSet):
    serializer_class = Celebrity_langSerializer
    queryset = Celebrity_lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class Role_langViewSet(viewsets.ModelViewSet):
    serializer_class = Role_langSerializer
    queryset = Role_lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class SagaViewSet(viewsets.ModelViewSet):
    serializer_class = SagaSerializer
    queryset = Saga.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class Saga_langViewSet(viewsets.ModelViewSet):
    serializer_class = Saga_langSerializer
    queryset = Saga_lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class Genre_langViewSet(viewsets.ModelViewSet):
    serializer_class = Genre_langSerializer
    queryset = Genre_lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class EmotionViewSet(viewsets.ModelViewSet):
    serializer_class = EmotionSerializer
    queryset = Emotion.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class Emotion_langViewSet(viewsets.ModelViewSet):
    serializer_class = Emotion_langSerializer
    queryset = Emotion_lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class StreamingViewSet(viewsets.ModelViewSet):
    serializer_class = StreamingSerializer
    queryset = Streaming.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class SourceViewSet(viewsets.ModelViewSet):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']
    # Search for users
    filter_backends = (filters.SearchFilter,)
    search_fields = ('original_title',)

class Movie_langViewSet(viewsets.ModelViewSet):
    serializer_class = Movie_langSerializer
    queryset = Movie_lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class CatalogueViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogueSerializer
    queryset = Catalogue.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class Catalogue_langViewSet(viewsets.ModelViewSet):
    serializer_class = Catalogue_langSerializer
    queryset = Catalogue_lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

class ParticipationViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipationSerializer
    queryset = Participation.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']
