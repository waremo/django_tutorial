from django.urls import path
from books.views import PublisherList, BookList, AuthorList
from books.views import PublisherDetailView, BookDetailView, AuthorDetailView

app_name = 'books'
urlpatterns = [
    path('publishers/', PublisherList.as_view()),
    path('publishers/<int:pk>/', PublisherDetailView.as_view()),
    path('books/', BookList.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('authors/', AuthorList.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view()),
]

