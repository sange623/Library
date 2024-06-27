from rest_framework import viewsets
from .models import Book
from .serializers import BooksSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializers
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter,DjangoFilterBackend,OrderingFilter]
    search_fields = ['id', 'name']
    filterset_fields = {
        'price' : ['exact', 'gte', 'lte'] 
    }

