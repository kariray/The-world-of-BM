from django.urls import path
from books.views import BooksView, BookDetail, BookCreate, BookDelete, BookUpdate

app_name = "books"

urlpatterns = [
    path("", BooksView.as_view(), name="books"),
    path("<int:pk>/", BookDetail.as_view(), name="book"),
    path("create/", BookCreate.as_view(), name="create"),
    path("update/<int:pk>/", BookUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", BookDelete.as_view(), name="delete"),
]
