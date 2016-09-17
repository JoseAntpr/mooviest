from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse
from .models import Movie, Movie_lang

def index(request, movie_id):
    movie =  get_object_or_404(Movie, pk = movie_id)
    print(movie_id)
    movie_lang = movie.get_movie_lang('es')
    celebs = movie.participations.all()
    return render(request, 'movie/index.html', {'movie': movie_lang, 'celebs': celebs})
