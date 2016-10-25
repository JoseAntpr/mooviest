from django.shortcuts import get_object_or_404, render, redirect
from movie.models import Movie, Movie_lang

def index(request):
    movies = Movie.objects.all()
    return render(request, 'home/index.html', {'recommendations': movies})
    #return render(request, 'home/index.html')

#def getRecommendations(request):
#    movies = Movie.objects.all()
#    return render(request, 'home/index.html', {'recommendations': movies})
