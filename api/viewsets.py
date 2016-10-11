from movie.models import Lang, Country, Celebrity, Celebrity_lang, Role, Role_lang, Saga, Saga_lang, Genre, Genre_lang, Emotion, Emotion_lang, Streaming, Source, Movie, Movie_lang, Rating, Catalogue, Catalogue_lang, Participation
from .serializers import LangSerializer, CountrySerializer, CelebritySerializer, Celebrity_langSerializer, RoleSerializer, Role_langSerializer, SagaSerializer, Saga_langSerializer, GenreSerializer, Genre_langSerializer, EmotionSerializer, Emotion_langSerializer, StreamingSerializer, SourceSerializer, MovieSerializer, Movie_langSerializer, RatingSerializer, CatalogueSerializer, Catalogue_langSerializer, ParticipationSerializer
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .serializers_custom import MovieCustomSerializer, MovieListCustomSerializer


class LangViewSet(viewsets.ModelViewSet):
    serializer_class = LangSerializer
    queryset = Lang.objects.all()


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

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

    def retrieve(self,request,pk=None):
        instance = Movie_lang.objects.get(pk=request.query_params.get('movie_lang'))
        serializer = MovieCustomSerializer(instance)

        return Response(serializer.data)

class Movie_langViewSet(viewsets.ModelViewSet):
    serializer_class = MovieListCustomSerializer
    queryset = Movie_lang.objects.all()
    http_method_names = ['get', 'post', 'head', 'put', 'patch']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

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
