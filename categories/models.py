from django.db import models
from django.db.models.fields import CharField
from core.models import CoreModel

# Create your models here.


class Category(CoreModel):
    """ Category model """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
