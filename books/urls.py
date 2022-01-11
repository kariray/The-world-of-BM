from django.urls import path
from books.views import BooksView, BookDetail

app_name = "books"

urlpatterns = [
    path("", BooksView.as_view(), name="books"),
    path("<int:pk>/", BookDetail.as_view(), name="book"),
]
