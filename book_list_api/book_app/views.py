from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_date']  # fields to search on

class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class ReviewListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book__id=book_id)