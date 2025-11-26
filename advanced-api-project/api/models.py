
from django.db import models

# Author model:
# Represents a book author. Each author can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's full name

    def __str__(self):
        return self.name


# Book model:
# Stores details about books written by authors.
# Each book belongs to one author (ForeignKey).
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book title
    publication_year = models.IntegerField()  # Year book was published
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE
    )  # One-to-many relationship

    def __str__(self):
        return self.title
