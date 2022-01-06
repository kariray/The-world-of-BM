from django.urls import path
from movies.views import MoviesView, MovieDetail, UpdateMovie, CreateMovie, DeleteMovie

app_name = "movies"

urlpatterns = [
    path("", MoviesView.as_view(), name="movies"),
    path("<int:pk>", MovieDetail.as_view(), name="movie"),
    path("<int:pk>/update", UpdateMovie.as_view(), name="update"),
    path("create/", CreateMovie.as_view(), name="create"),
    path("<int:pk>/delete", DeleteMovie.as_view(), name="delete"),
]
