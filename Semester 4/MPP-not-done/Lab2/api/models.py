from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, default=1) #many to one
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    library = models.ForeignKey('Library', on_delete=models.PROTECT, default=1) #many to one

    def __str__(self):
        return "ISBN: " + str(self.isbn) + " Title: " + self.title + " Author: " + self.author + " Genre: " + self.genre.name + " Pages: " + str(self.pages) + " Price: " + str(self.price) + " Library: " + self.library.name
    
class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey('Address', on_delete=models.PROTECT)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return "Name: " + self.name + " Address: " + self.address 
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    descripiton = models.CharField(max_length=100)
    popularity = models.IntegerField()
    age_group = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=5)
    
    def __str__(self):
        return "Name: " + self.name + " Description: " + self.descripiton
    

# many to many relation between the entities of book and library. 
class Borrowed(models.Model):
    library = models.ForeignKey('Library', on_delete=models.PROTECT)
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    reader = models.ForeignKey('Reader', on_delete=models.PROTECT, default=1)
    days_borrowed = models.IntegerField()
    extra_days = models.IntegerField()
    
    def __str__(self):
        return "Library: " + self.library.name + " Book: " + self.book.title + " Reader: " + self.reader.name + " Days Borrowed: " + str(self.days_borrowed) + " Extra Days: " + str(self.extra_days)

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