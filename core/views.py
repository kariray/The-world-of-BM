from django.shortcuts import render
from movies.models import Movie

# Create your views here.


def home(request):

    movies = Movie.objects.all().order_by('-pk')[:10]
    return render(request, "home.html", {"movies": movies, })
