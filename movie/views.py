from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse
from .models import Movie, Movie_lang

def index(request, movie_id):
    movie =  get_object_or_404(Movie, pk = movie_id, movie_lang = 'es')
    return render(request, 'movie/index.html', {'movie': movie})

