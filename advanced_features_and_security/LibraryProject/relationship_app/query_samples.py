import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from LibraryProject.relationship_app.models import Author, Book, Library, Librarian


author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George R.R. Martin")

book1 = Book.objects.create(title="Harry Potter", author=author1)
book2 = Book.objects.create(title="Harry Potter 2", author=author1)
book3 = Book.objects.create(title="Game of Thrones", author=author2)

library = Library.objects.create(name="Central Library")
library.books.set([book1, book3])

librarian = Librarian.objects.create(name="Alice", library=library)




author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name, ":", [book.title for book in books_by_author])



library_name = "Central Library"
library = Library.objects.get(name=library_name)
library_books = library.books.all()
print(f"Books in {library_name}:", [book.title for book in library_books])


library_name = "Central Library"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print("Librarian of", library_name, ":", librarian.name)
