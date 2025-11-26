from rest_framework import serializers
from .models import Author, Book
import datetime


# BookSerializer:
# Serializes all book fields and includes custom validation
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# AuthorSerializer:
# Includes name and nested list of books using BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    # Nesting books: read-only, DRF automatically fetches related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

"""
How the relationship works:
- Author has a ForeignKey relationship to Book (one author -> many books)
- related_name="books" in the Book model allows accessing all books via author.books
- The AuthorSerializer nests BookSerializer using books = BookSerializer(many=True)
"""
