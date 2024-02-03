from django.contrib import admin
from .models import Book, Genre, Library, Borrowed

# Register your models here.
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Genre)
admin.site.register(Borrowed)
