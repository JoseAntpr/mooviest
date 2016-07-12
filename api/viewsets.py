from movie.models import Lang, Country, Celebrity, Celebrity_lang, Role, Role_lang, Saga, Saga_lang, Genre, Genre_lang, Emotion, Emotion_lang, Streaming, Source, Movie, Movie_lang, Rating, Catalogue, Catalogue_lang, Participation
from .serializers import LangSerializer, CountrySerializer, CelebritySerializer, Celebrity_langSerializer, RoleSerializer, Role_langSerializer, SagaSerializer, Saga_langSerializer, GenreSerializer, Genre_langSerializer, EmotionSerializer, Emotion_langSerializer, StreamingSerializer, SourceSerializer, MovieSerializer, Movie_langSerializer, RatingSerializer, CatalogueSerializer, Catalogue_langSerializer, ParticipationSerializer
from rest_framework import viewsets


class LangViewSet(viewsets.ModelViewSet):
    serializer_class = LangSerializer
    queryset = Lang.objects.all()

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class CelebrityViewSet(viewsets.ModelViewSet):
    serializer_class = CelebritySerializer
    queryset = Celebrity.objects.all()

class Celebrity_langViewSet(viewsets.ModelViewSet):
    serializer_class = Celebrity_langSerializer
    queryset = Celebrity_lang.objects.all()

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

class Role_langViewSet(viewsets.ModelViewSet):
    serializer_class = Role_langSerializer
    queryset = Role_lang.objects.all()

class SagaViewSet(viewsets.ModelViewSet):
    serializer_class = SagaSerializer
    queryset = Saga.objects.all()

class Saga_langViewSet(viewsets.ModelViewSet):
    serializer_class = Saga_langSerializer
    queryset = Saga_lang.objects.all()

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class Genre_langViewSet(viewsets.ModelViewSet):
    serializer_class = Genre_langSerializer
    queryset = Genre_lang.objects.all()

class EmotionViewSet(viewsets.ModelViewSet):
    serializer_class = EmotionSerializer
    queryset = Emotion.objects.all()

class Emotion_langViewSet(viewsets.ModelViewSet):
    serializer_class = Emotion_langSerializer
    queryset = Emotion_lang.objects.all()

class StreamingViewSet(viewsets.ModelViewSet):
    serializer_class = StreamingSerializer
    queryset = Streaming.objects.all()

class SourceViewSet(viewsets.ModelViewSet):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class Movie_langViewSet(viewsets.ModelViewSet):
    serializer_class = Movie_langSerializer
    queryset = Movie_lang.objects.all()

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

class CatalogueViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogueSerializer
    queryset = Catalogue.objects.all()

class Catalogue_langViewSet(viewsets.ModelViewSet):
    serializer_class = Catalogue_langSerializer
    queryset = Catalogue_lang.objects.all()

class ParticipationViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipationSerializer
    queryset = Participation.objects.all()
