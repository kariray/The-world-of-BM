from django.db import models
from core.models import CoreModel

# Create your models here.


class Review(CoreModel):
    """ Review Model """
    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()

    def __str__(self):
        return self.text
