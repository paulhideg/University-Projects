from rest_framework import serializers
from .models import Book, Genre, Library, Borrowed, Reader, Address

#turns the django database model in json
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('__all__')

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('__all__')

class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowed
        fields = ('__all__')

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ('__all__')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')