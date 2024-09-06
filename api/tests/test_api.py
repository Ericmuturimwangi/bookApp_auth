from django.test import TestCase
from rest_framework.test import APIClient
from .models import Book


class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title="Test Book", author="Test Author", publication_year=2022
        )

    def test_get_all_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_create_book(self):
        data = {"title": "New Book", "author": "New Author", "publication_year": 2023}
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 2)
