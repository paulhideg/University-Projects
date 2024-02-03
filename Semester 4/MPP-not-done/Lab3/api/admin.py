from django.contrib import admin
from .models import Book, Genre, Library, Borrowed, Reader, Address

# Register your models here.
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Genre)
admin.site.register(Borrowed)
admin.site.register(Reader)
admin.site.register(Address)