from movie.models import Celebrity
from .serializers import CelebritySerializer
from rest_framework import generics
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
