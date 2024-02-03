from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Book, Genre, Library, Borrowed, Reader, Address

# Create your tests here.
class TestBookStats(APITestCase):
    url='/api/books-stats/'

    #add book
    def setUp(self):
        Address.objects.create(street='test', street_number=1, city='test')
        Library.objects.create(name='test', address_id=1, phone='test', email='test', capacity=100)
        Genre.objects.create(name='test', description='test', popularity=1, age_group='test', rating=1)
        Reader.objects.create(name='test')

        Book.objects.create(isbn=123123123,title='test', author='test', genre_id=1, library_id=1, pages=100, price=20)
        Borrowed.objects.create(reader_id=1, book_id=1, days_borrowed=1, extra_days=1)
        Borrowed.objects.create(reader_id=1, book_id=1, days_borrowed=3, extra_days=2)

        Book.objects.create(isbn=123123123,title='test2', author='test', genre_id=1, library_id=1, pages=300, price=30)
        Borrowed.objects.create(reader_id=1, book_id=2, days_borrowed=5, extra_days=2)

    def test_book_stats(self):
        response = self.client.get('/api/books-stats/')
        result = response.json()
        #print(result)
        
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(result[0]["book"], 'test')
        self.assertEqual(result[1]["book"], 'test2')
        self.assertEqual(result[0]["borrows"], 2)
        self.assertEqual(result[1]["borrows"], 1)

class TestGenreStats(APITestCase):
    url='/api/genres-stats/'

    #add genre
    def setUp(self):
        Address.objects.create(street='test', street_number=1, city='test')
        Library.objects.create(name='test', address_id=1, phone='test', email='test', capacity=100)
        Genre.objects.create(name='test', description='test', popularity=1, age_group='10+', rating=5)
        Genre.objects.create(name='test2', description='test', popularity=5, age_group='5+', rating=7)
        Book.objects.create(isbn=123123123,title='test', author='test', genre_id=1, library_id=1, pages=100, price=20)
        Book.objects.create(isbn=123321123,title='test2', author='test', genre_id=2, library_id=1, pages=356, price=30)
        

    def test_genre_stats(self):
        response = self.client.get('/api/genres-stats/')
        result = response.json()
        print(result)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]["genre"], 'test2')
        self.assertEqual(response.data[1]["genre"], 'test')
        self.assertEqual(response.data[0]["totalPages"], 356)
        self.assertEqual(response.data[1]["totalPages"], 100)

    
