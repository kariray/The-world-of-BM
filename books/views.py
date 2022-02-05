from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, DeleteView, UpdateView
from books.models import Book
from . import forms


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


class BookCreate(FormView):
    """ Create new books"""
    form_class = forms.CreateBookForm
    template_name = "books/book_create.html"

    def get(self, request):
        form = self.get_form()
        return render(request, "books/book_create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():

            book = form.save()
            book.save()
            return redirect(reverse("books:book", kwargs={"pk": book.pk}))
        else:

            return render(request, "books/book_create.html", {"form": form})


class BookUpdate(UpdateView):
    model = Book
    template_name = "books/book_update.html"
    success_url = reverse_lazy("books:books")
    fields = ("title",
              "year",
              "rating",
              "cover_image",
              "category",
              "writer",
              "storyline",)


class BookDelete(DeleteView):
    """ Delete book information """
    model = Book
    success_url = reverse_lazy("books:books")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
