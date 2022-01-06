from django.core.paginator import Paginator
from django.views.generic import ListView
from django.shortcuts import render
from movies.models import Movie

# Create your views here.


class MoviesView(ListView):
    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created_at"
    context_object_name = "movies"
