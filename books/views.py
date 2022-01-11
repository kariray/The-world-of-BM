from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
