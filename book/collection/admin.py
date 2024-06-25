from django.contrib import admin
from collection.models import Book,Articles

# Register your models here.
admin.site.register([Book,Articles])