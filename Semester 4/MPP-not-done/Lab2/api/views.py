from rest_framework import generics
from .models import Book, Genre, Library, Borrowed, Reader, Address
from .serializers import BookSerializer, GenreSerializer, LibrarySerializer, BorrowedSerializer, ReaderSerializer, AddressSerializer

# Create your views here.

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        givenPages = self.request.query_params.get('pages')
        if givenPages is not None:
            queryset = queryset.filter(pages__gt=givenPages)
        return queryset
    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class GenreList(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class LibraryList(generics.ListCreateAPIView):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

class LibraryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()

class BorrowedList(generics.ListCreateAPIView):
    serializer_class = BorrowedSerializer
    queryset = Borrowed.objects.all()

class BorrowedDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BorrowedSerializer
    queryset = Borrowed.objects.all()

class ReaderList(generics.ListCreateAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()

class ReaderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()

class AddressList(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()