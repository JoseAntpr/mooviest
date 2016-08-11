from movie.models import Celebrity, Movie
from .serializers import CelebritySerializer, MovieSerializer
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
