from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


Author = get_user_model()

class Articles(models.Model):
    article_name = models.CharField(max_length=30)

    def __str__(self):
        return self.article_name


class Book(models.Model):
    book_name = models.CharField(max_length=20)
    price = models.IntegerField()
    auther = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    articles = models.ManyToManyField(Articles)

    def __str__(self):
        return self.book_name


