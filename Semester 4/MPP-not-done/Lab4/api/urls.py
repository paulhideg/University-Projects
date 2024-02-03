from django.urls import path, include
from .views import BookView, GenreView, LibraryView, BorrowedView, ReaderView, AddressView, GenreStatsView, BookStatsView, LibraryBooksView, AddressLibraryView, GenreBooksView, BookBorrowsView, ReaderBorrowsView, BookReadersView, BorrowedBooksView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('addresses', AddressView)
router.register('libraries', LibraryView)
router.register('genres', GenreView)
router.register('books', BookView)
router.register('readers', ReaderView)
router.register('borrows', BorrowedView)

urlpatterns = [
    path('', include(router.urls)),
    path('genres-stats/', GenreStatsView.as_view(), name='genres-stats'),
    path('books-stats/', BookStatsView.as_view(), name='books-stats'),
    path('library/<int:library_id>/books/', LibraryBooksView.as_view(), name='library_books'),#onetomany
    path('address/<int:address_id>/libraries/', AddressLibraryView.as_view(), name='address_libraries'),#onetoone
    path('genre/<int:genre_id>/books/', GenreBooksView.as_view(), name='genre_books'),#onetomany
    path('book/<int:book_id>/borrows/', BookBorrowsView.as_view(), name='book_borrows'),#onetomany
    path('reader/<int:reader_id>/borrows/', ReaderBorrowsView.as_view(), name='reader_borrows'),#onetomany
    path('book/<int:book_id>/readers/', BookReadersView.as_view(), name='book_readers'),#manytomany
    path('reader/<int:reader_id>/books/', BorrowedBooksView.as_view(), name='reader_books'),#manytomany
]
