from rest_framework import serializers
from .models import Book

#turns the django database model in json
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')