from django.shortcuts import get_object_or_404, render, redirect
from movie.models import Movie, Movie_lang, Lang

def index(request):
    recommendations = getMovie(1, 'es')
    return render(request, 'home/index.html', {'recommendations': recommendations})

def getMovie(id, lang):
    movie = Movie_lang.objects.select_related('movie').get(lang__code = lang, movie__id = id)
    return movie