from django.shortcuts import get_object_or_404, render, redirect
from movie.models import Movie, Movie_lang, Lang
from django.db.models import Prefetch

def index(request):
    recommendations = getRecommendations()
    #movies = Movie_lang.objects.filter(lang__code = 'es').select_related('movie')
    #print(movies[0].movie_lang.get(lang_code = 'es').title)
    return render(request, 'home/index.html', {'recommendations': recommendations})

def getRecommendations():
    # Recommendations = all movies at the moment
    recommendations = list(Movie_lang.objects.filter(lang__code = 'en').select_related('movie'))
    return recommendations

def getMovie():
    movie = Movie.objects.get(id = 1)
    movieLang = movie.get_movie_lang('es')

def nextMovie():
    print (getRecommendations()[3].image)
    return getRecommendations()[3]
