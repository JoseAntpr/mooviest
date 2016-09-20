from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse
from .models import Movie, Movie_lang
from users.models import Profile, User, Collection

def index(request, movie_id):
    movie =  get_object_or_404(Movie, pk = movie_id)
    movie_lang = movie.get_movie_lang('en')
    celebs = movie.participations.filter(movie = movie.pk)
    # typemovie = string with collection its in
    typeMovie = request.user.profile.get_typemovie(movie).name
    return render(request, 'movie/index.html', {'movie': movie_lang, 'celebs': celebs, 'collection': typeMovie})
