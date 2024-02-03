from django.shortcuts import render
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework import viewsets, views
from .models import Book, Genre, Library, Borrowed, Reader, Address
from .serializers import BookSerializer, GenreSerializer, LibrarySerializer, BorrowedSerializer, ReaderSerializer, AddressSerializer

# Create your views here.

class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    # def get_queryset(self):
    #     queryset = Book.objects.all()
        # givenPages = self.request.query_params.get('pages')
        # if givenPages is not None:
        #     queryset = queryset.filter(pages__gt=givenPages)
        # return queryset
    
class GenreView(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class LibraryView(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

class BorrowedView(viewsets.ModelViewSet):
    serializer_class = BorrowedSerializer
    queryset = Borrowed.objects.all()

class ReaderView(viewsets.ModelViewSet):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()

class AddressView(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

#create a view to get the books sorted by the most borrows
class BookStatsView(views.APIView):
    def get(self, request):
        books = Book.objects.all()
        bookStats = []
        for book in books:
            bookStats.append({
                'book': book.title,
                'borrows': Borrowed.objects.filter(book=book).count()
            })
        bookStats.sort(key=lambda x: x['borrows'], reverse=True)
        return Response(bookStats)

#create a view to get the genres sorted by the average pages of books from that genre
class GenreStatsView(views.APIView):
    def get(self, request):
        genres = Genre.objects.all()
        genreStats = []
        for genre in genres:
            genreStats.append({
                'genre': genre.name,
                'averagePages': Book.objects.filter(genre=genre).aggregate(Avg('pages'))['pages__avg']
            })
        genreStats.sort(key=lambda x: x['averagePages'], reverse=True)
        return Response(genreStats)
    

#display one entity of library and the books entities that are related to it
class LibraryBooksView(views.APIView):
    def get(self, request, library_id):
        library = Library.objects.get(id=library_id)
        books = Book.objects.filter(library=library)
        data = {
            'library': {
                'id': library.id,
                'name': library.name,
            },
            'books': BookSerializer(books, many=True).data,
        }
        return Response(data)
    
#display one entity of address and the library entity that is related to it
class AddressLibraryView(views.APIView):
    def get(self, request, address_id):
        address = Address.objects.get(id=address_id)
        library = Library.objects.get(id=address.library.id)
        data = {
            'address': {
                'id': address.id,
                'street': address.street,
                'street_number': address.street_number,
                'city': address.city,
            },
            'library': {
                'id': library.id,
                'name': library.name,
            }
        }
        return Response(data)
    
#display one entity of genre and the books entities that are related to it
class GenreBooksView(views.APIView):
    def get(self, request, genre_id):
        genre = Genre.objects.get(id=genre_id)
        books = Book.objects.filter(genre=genre)
        data = {
            'genre': {
                'id': genre.id,
                'name': genre.name,
            },
            'books': BookSerializer(books, many=True).data,
        }
        return Response(data)
    
#display one entity of book and the borrowed entities that are related to it
class BookBorrowsView(views.APIView):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        borrows = Borrowed.objects.filter(book=book)
        data = {
            'book': {
                'id': book.id,
                'title': book.title,
            },
            'borrows': BorrowedSerializer(borrows, many=True).data,
        }
        return Response(data)
    
#display one entity of reader and the borrowed entities that are related to it
class ReaderBorrowsView(views.APIView):
    def get(self, request, reader_id):
        reader = Reader.objects.get(id=reader_id)
        borrows = Borrowed.objects.filter(reader=reader)
        data = {
            'reader': {
                'id': reader.id,
                'name': reader.name,
            },
            'borrows': BorrowedSerializer(borrows, many=True).data,
        }
        return Response(data)
    
#display one entity of book and the reader entities that are related to it
class BookReadersView(views.APIView):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        borrows = Borrowed.objects.filter(book=book)
        readers = []
        for borrow in borrows:
            readers.append(borrow.reader)
        data = {
            'book': {
                'id': book.id,
                'title': book.title,
            },
            'readers': ReaderSerializer(readers, many=True).data,
        }
        return Response(data)
    
#display one entity of borrowed and the book entities that are related to it
class BorrowedBooksView(views.APIView):
    def get(self, request, borrowed_id):
        borrowed = Borrowed.objects.get(id=borrowed_id)
        book = Book.objects.get(id=borrowed.book.id)
        data = {
            'borrowed': {
                'id': borrowed.id,
                'date': borrowed.date,
            },
            'book': {
                'id': book.id,
                'title': book.title,
            }
        }
        return Response(data)