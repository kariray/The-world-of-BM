from django.db import models
from core.models import CoreModel

# Create your models here.


class Book(CoreModel):

    """ Book Model """

    title = models.CharField(max_length=120)
    year = models.IntegerField()
    rating = models.IntegerField()
    cover_image = models.ImageField(
        null=True, blank=True, upload_to="book_cover")
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="books")
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="books")
    storyline = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def cut_storyline(self):
        if len(self.storyline) >= 300:
            preview = self.storyline[:300]
            read_more = self.storyline[300:]
            return {"preview": preview, "read_more": read_more}
