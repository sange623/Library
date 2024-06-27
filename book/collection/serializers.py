from rest_framework import serializers
from .models import Book,Articles

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
