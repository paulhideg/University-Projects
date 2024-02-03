from django.db import models
from rest_framework import serializers

def TitleValidator(value):
    if len(value) > 3:
        return value
    else:
        raise serializers.ValidationError("The title must have at least three characters")

def AuthorValidator(value):
    if len(value) > 3:
        return value
    else:
        raise serializers.ValidationError("The author must have at least three characters")

def PageValidator(value):
    if value > 0:
        return value
    else:
        raise serializers.ValidationError("The number of pages must be greater than 0")

# Create your models here.
class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100, validators=[TitleValidator])
    author = models.CharField(max_length=100, validators=[AuthorValidator])
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, default=1) #many to one
    pages = models.IntegerField(validators=[PageValidator])
    price = models.DecimalField(max_digits=5, decimal_places=2)
    library = models.ForeignKey('Library', on_delete=models.PROTECT, default=1) #many to one

    def __str__(self):
        return "ISBN: " + str(self.isbn) + " Title: " + self.title + " Author: " + self.author + " Genre: " + self.genre.name + " Pages: " + str(self.pages) + " Price: " + str(self.price) + " Library: " + self.library.name 
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField('Address', on_delete=models.DO_NOTHING) #one to one
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return "Name: " + self.name + " Address: " + self.address.street + " Phone: " + self.phone + " Email: " + self.email + " Capacity: " + str(self.capacity)
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    popularity = models.IntegerField()
    age_group = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=5)
    
    def __str__(self):
        return "Name: " + self.name + " Description: " + self.description + " Popularity: " + str(self.popularity) + " Age Group: " + self.age_group + " Rating: " + str(self.rating)
    

# many to many relation between the entities of book and reader. 
class Borrowed(models.Model):
    days_borrowed = models.IntegerField()
    extra_days = models.IntegerField()
    book = models.ForeignKey('Book', on_delete=models.PROTECT, default=1)
    reader = models.ForeignKey('Reader', on_delete=models.PROTECT, default=1)
    
    def __str__(self):
        return "Days Borrowed: " + str(self.days_borrowed) + " Extra Days: " + str(self.extra_days) + " Book: " + self.book.title + " Reader: " + self.reader.name
    
class Reader(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return "Name: " + self.name 
    
class Address(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return "Street: " + self.street + " Street Number: " + str(self.street_number) + " City: " + self.city