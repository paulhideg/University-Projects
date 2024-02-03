from django.urls import path
from .views import BookList, BookDetail, GenreList, GenreDetail, LibraryList, LibraryDetail, BorrowedList, BorrowedDetail, ReaderList, ReaderDetail, AddressList, AddressDetail

urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),
    path('genre/', GenreList.as_view()),
    path('genre/<int:pk>/', GenreDetail.as_view()),
    path('library/', LibraryList.as_view()),
    path('library/<int:pk>/', LibraryDetail.as_view()),
    path('borrowed/', BorrowedList.as_view()),
    path('borrowed/<int:pk>/', BorrowedDetail.as_view()),
    path('reader/', ReaderList.as_view()),
    path('reader/<int:pk>/', ReaderDetail.as_view()),
    path('address/', AddressList.as_view()),
    path('address/<int:pk>/', AddressDetail.as_view()),
]
