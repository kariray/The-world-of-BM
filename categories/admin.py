from django.contrib import admin
from django.contrib.admin.decorators import register
from categories.models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    list_filter = (
        "name",
    )
