from django.db import models
from django.db.models.fields import CharField
from core.models import CoreModel

# Create your models here.


class Category(CoreModel):
    """ Category model """

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"

    KIND_CHOICE = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
    )

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=15, choices=KIND_CHOICE)

    def __str__(self):
        return self.name
