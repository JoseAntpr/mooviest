from django.shortcuts import get_object_or_404, render, redirect
from django.http  import HttpResponse
import json
from django.db.models import Q
from .models import Movie, Movie_lang
from users.models import Profile, User, Collection, TypeMovie

def index(request, movie_id):
    movie =  get_object_or_404(Movie, pk = movie_id)
    movie_lang = movie.get_movie_lang('en')
    celebs = movie.participations.filter(movie = movie.pk)
    # typemovie = string with collection its in
    user = request.user
    if user.is_authenticated():
        typeMovie = user.profile.get_typemovie(movie)
        if (typeMovie):
            typeMovie = typeMovie.name
    else:
        typeMovie = None
    return render(request, 'movie/index.html', {'movie': movie_lang, 'celebs': celebs, 'collection': typeMovie})

def changeCollection(request, movie_id):
    movie =  get_object_or_404(Movie, pk = movie_id)
    user = request.user
    if user.is_authenticated():
        typeMovie = user.profile.get_typemovie(movie)
        btnPressed = ''
        if 'seen' in request.POST:
            btnPressed = 'seen'
        elif 'not-seen' in request.POST:
            btnPressed = 'not-seen'
        elif 'favourite' in request.POST:
            btnPressed = 'favourite'
        elif 'watchlist' in request.POST:
            btnPressed = 'watchlist'

        if typeMovie:
            typeMovie.name = btnPressed
            typeMovie.save()
        else:
            collection = Collection()
            collection.movie = movie
            collection.user = request.user.profile
            typeMovie = TypeMovie()
            typeMovie.name = btnPressed
            typeMovie.save()
            collection.typeMovie = typeMovie
            collection.save()
    else:
        print("ERROR: user does not exist")

    return redirect('/movie/' + movie_id)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        movies = Movie_lang.objects.filter(Q(title__icontains = q) | Q(movie__original_title__icontains = q),lang__code = request.LANGUAGE_CODE).value(title)
        if len(movies) == 1:
            return redirect ('movie',movie_id=movies[0].id)
        else:
            return render(request,'movie/search.html',{'movies':movies, 'query': q})
    else:
        return HttpResponde("You Submmited an empty form.")

def busqueda(request):
    print(hol111)
    if request.is_ajax():
        print(hola)
        q = request.GET['q']
        movies = Movie_lang.objects.filter(Q(title__icontains = q) | Q(movie__original_title__icontains = q),lang__code = request.LANGUAGE_CODE).value(title)
        if len(movies) == 1:
            return redirect ('movie',movie_id=movies[0].id)
        else:
            return render(request,'movie/search.html',{'movies':movies, 'query': q})
    else:
        return HttpResponde("You Submmited an empty form.")
