from movie.models import Celebrity, Movie
from .serializers import CelebritySerializer, MovieSerializer
from .serializers_custom import MovieAppSerializer
from rest_framework import generics, filters, viewsets
import urllib.parse

class CelebrityCustomViewSet(generics.ListAPIView):
    serializer_class = CelebritySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        n = urllib.parse.unquote_plus(self.kwargs['name'])
        print(n)
        return Celebrity.objects.filter(name=n)

class MovieByReleasedViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=released',)

class MoviesAppByLangViewSet(generics.ListAPIView):
    serializer_class = MovieAppSerializer
    lang = 1
    def get_queryset(self):
        l = self.request.query_params.get('lang_id', None)
        movie_id = self.request.query_params.get('id', None)
        queryset = Movie.objects.filter(pk=movie_id)
        self.lang = l
        return queryset

    def get_serializer_context(self):
        return {'lang': self.lang}
