from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from books.models import Book, Publisher, Author

class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'

class AuthorList(ListView):
    queryset = Author.objects.order_by('-name')
    context_object_name = 'author_list'

class PublisherList(ListView):
    model = Publisher

class PublisherBookList(ListView):

    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)

class BookDetailView(DetailView):
    model = Book

class AuthorDetailView(DetailView):

    queryset = Author.objects.all()

    def get_object(self):
        # Call the superclass
        object = super().get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object

class PublisherDetailView(DetailView):
    model = Publisher
# Create your views here.
