from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework        
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# -------------------------
# LIST VIEW
# -------------------------
class ListView(generics.ListAPIView):
    """
    Retrieve all books (read-only) with:
    - filtering (title, author, publication_year)
    - search (title, author name)
    - ordering (title, publication_year)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filters
    filter_backends = [
        DjangoFilterBackend,  # filtering
        filters.SearchFilter,  # searching
        filters.OrderingFilter # ordering
    ]

    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# -------------------------
# DETAIL VIEW
# -------------------------
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -------------------------
# CREATE VIEW
# -------------------------
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------------
# UPDATE VIEW
# -------------------------
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------------
# DELETE VIEW
# -------------------------
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
