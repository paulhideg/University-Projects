from rest_framework import serializers
from .models import Book, Genre, Library, Borrowed, Reader, Address

#turns the django database model in json
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('id','name', 'description', 'popularity', 'age_group', 'rating', 'url')

class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = ('id','name', 'address', 'phone', 'email', 'capacity', 'url')

class BorrowedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Borrowed
        fields = ('id','reader', 'book', 'days_borrowed', 'extra_days', 'url')
        #depth = 1

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ('__all__')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id','street', 'street_number', 'city', 'url')


