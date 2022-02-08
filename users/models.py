from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    PREF_BOOKS = "books"
    PREF_MOVIES = "movies"
    PREF_CHOICES = (
        (PREF_BOOKS, "Books"),
        (PREF_MOVIES, "Movies"),
    )

    LANG_EN = "english"
    LANG_KO = "korean"
    LANG_JP = "japaness"
    LANG_CHOICES = (
        (LANG_EN, "English"),
        (LANG_KO, "Korean"),
        (LANG_JP, "Japaness"),
    )

    bio = models.TextField()
    avatar = models.ImageField(
        null=True, blank=True, upload_to="user_avatar")
    preference = models.CharField(
        max_length=10, choices=PREF_CHOICES, default=PREF_MOVIES)
    language = models.CharField(
        max_length=20, choices=LANG_CHOICES, default=LANG_EN)
    fav_book_genre = models.ForeignKey(
        "categories.Category", on_delete=models.SET_NULL, null=True, related_name="book_users")
    fav_movie_genre = models.ForeignKey(
        "categories.Category", on_delete=models.SET_NULL, null=True, related_name="movie_users")

    def __str__(self):
        return self.username
