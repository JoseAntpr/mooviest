from movie.models import Lang, Country, Celebrity, Celebrity_lang, Role, Role_lang, Saga, Saga_lang, Genre, Genre_lang, Emotion, Emotion_lang, Streaming, Source, Movie, Movie_lang, Rating, Catalogue, Catalogue_lang, Participation
from users.models import Collection
from .serializers import LangSerializer, CountrySerializer, CelebritySerializer, Celebrity_langSerializer, RoleSerializer, Role_langSerializer, SagaSerializer, Saga_langSerializer, GenreSerializer, Genre_langSerializer, EmotionSerializer, Emotion_langSerializer, StreamingSerializer, SourceSerializer, MovieSerializer, Movie_langSerializer, RatingSerializer, CatalogueSerializer, Catalogue_langSerializer, ParticipationSerializer
from .serializers_custom import MovieListCustomSerializer, RatingAppSerializer, ParticipationAppSerializer, GenreAppSerializer

from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def retrieve(self,request,pk=None):

        movie_lang = Movie_lang.objects.get(pk=request.query_params.get('movie_lang_id'))
        movie = movie_lang.movie

        # ratings = []
        # for r in Rating.objects.filter(movie = movie).select_related('movie'):
        #     ratings.append(
        #         {
        #             'name': r.name,
        #             'rating': r.rating,
        #             'count': r.count,
        #             'date_update': r.date_update
        #         }
        #     )

        ratings = Rating.objects.filter(movie=movie)
        ratingsSerializer = RatingAppSerializer(source='rating_set', many=True, instance = ratings)

        participations = Participation.objects.filter(movie = movie)
        participationSerializer = ParticipationAppSerializer(source='participation_set', many=True, instance = participations, context={'lang':movie_lang.lang.id})

        genres = Genre.objects.filter(movie = movie)
        genresSerializer = GenreAppSerializer(source='rating_set', many=True, instance = genres, context={'lang':movie_lang.lang.id})

        try:
            getCollection = Collection.objects.get(movie = movie_lang.movie, user = request.query_params.get('user_id'))
            collection = {
                'id': getCollection.id,
                'typeMovie': getCollection.typeMovie.name
            }

        except:
            collection = None

        return Response(
            {
                'id': movie.id,
                'movie_lang_id': movie_lang.id,
                'average': movie.average,
                'synopsis': movie_lang.synopsis,
                'collection': collection,
                'original_title': movie.original_title,
                'title': movie_lang.title,
                'runtime': movie.runtime,
                'released': movie.released,
                'backdrop': movie.backdrop,
                'image': movie_lang.image,
                'movie_producer': movie.movie_producer,
                'genres': genresSerializer.data,
                'country': None,
                'ratings': ratingsSerializer.data,
                'participations': participationSerializer.data
            }
        )

class Movie_langViewSet(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    serializer_class = MovieListCustomSerializer
    queryset = Movie_lang.objects.all()

    def get_queryset(self):
        queryset = Movie_lang.objects.all()

        title = self.request.query_params.get('title',None)
        code = self.request.query_params.get('code',None)
        print (title)
        if title is not None:
            queryset = Movie_lang.objects.filter(Q(title__icontains = title) | Q(movie__original_title__icontains = title),lang__code = code).order_by('id')
        return queryset
    #filter_backends = (filters.SearchFilter,)
    #search_fields = ('title',)

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

class MovieBasicViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
