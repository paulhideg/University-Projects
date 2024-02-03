from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        '''
        filter by price
        
        givenPages = self.request.query_params.get('pages')
        if price is not None:
            queryset = queryset.filter(pages < givenPages)
        '''
        return queryset
    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
