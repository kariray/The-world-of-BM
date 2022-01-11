from django.shortcuts import render
from movies.models import Movie
from books.models import Book

# Create your views here.


def home(request):

    movies = Movie.objects.all().order_by('-pk')[:10]
    books = Book.objects.all().order_by('-pk')[:10]
    return render(request, "home.html", {"movies": movies, "books": books, })
