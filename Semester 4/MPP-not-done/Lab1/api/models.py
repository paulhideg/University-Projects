from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    library = models.ForeignKey('Library', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return "ISBN: " + str(self.isbn) + " Title: " + self.title + " Author: " + self.author + " Genre: " + str(self.genre) + " Pages: " + str(self.pages) + " Price: " + str(self.price) + " Library: " + str(self.library)

class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    books = models.IntegerField()

    def __str__(self):
        return "Name: " + self.name + " Address: " + self.address + " Phone: " + self.phone + " Email: " + self.email + " Books: " + str(self.books)
    
class Genre(models.Model):
    name = models.CharField(max_length=100)
    descripiton = models.CharField(max_length=100)
    popularity = models.IntegerField()
    age_group = models.CharField(max_length=100)
    books = models.IntegerField()
    
    def __str__(self):
        return "Name: " + self.name + " Description: " + self.descripiton + " Popularity: " + str(self.popularity) + " Age Group: " + self.age_group + " Books: " + str(self.books)