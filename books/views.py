from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from books.models import Book


# Create your views here.
class BooksView(ListView):
    """Show the Book lists"""

    model = Book
    paginate_by = 10
    paginate_orphans = 5
    ordering = "-created_at"
    context_object_name = "books"


class BookDetail(DetailView):
    """Show the book detail"""

    model = Book
    context_object_name = "book"


class BookCreate(CreateView):
    """ Create new books"""
    model = Book
    fields = {
        "title",
        "year",
        "rating",
        "cover_image",
        "category",
        "writer",
        "storyline",
    }

    def get_success_url(self):
        book_pk = self.object.id
        return reverse("books:book", kwargs={"pk": book_pk})


class BookDelete(DeleteView):
    """ Delete book information """
    model = Book
    success_url = reverse_lazy("books:books")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
