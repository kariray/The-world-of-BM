from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render
from movies.models import Movie

# Create your views here.


class MoviesView(ListView):
    """Show the Movie lists"""

    model = Movie
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created_at"
    context_object_name = "movies"


class MovieDetail(DetailView):
    """ Show the movie details"""
    model = Movie
    context_object_name = "movie"


class UpdateMovie(UpdateView):
    """ Edit Movie's information """
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )

    def get_success_url(self):
        movie_pk = self.kwargs.get("pk")
        print(movie_pk)
        return reverse("movies:movie", kwargs={"pk": movie_pk})


class CreateMovie(CreateView):
    """ Create Movie's information """
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )

    def get_success_url(self):
        return reverse("movies:movies")


class DeleteMovie(DeleteView):
    """Delete Movie's information"""
    model = Movie
    success_url = reverse_lazy("movies:movies")
