from django.urls import path
from movies.views import MoviesView

app_name = "movies"

urlpatterns = [
    path("", MoviesView.as_view(), name="movies"),
]
