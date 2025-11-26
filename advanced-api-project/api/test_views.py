from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book
from django.contrib.auth.models import User


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Create an author
        self.author = Author.objects.create(name="Author 1")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2021
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2020
        }
        response = self.client.post(url, data)

        # Because in your views.py you are using IsAuthenticated → returns 403
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse('book-delete', kwargs={'pk': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
