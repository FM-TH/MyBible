from django.db import models
import datetime

# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length=20)
    keyword1 = models.CharField(max_length=10)
    keyword2 = models.CharField(max_length=10,null=True)
    keyword3 = models.CharField(max_length=10,null=True)
    comment = models.CharField(max_length=140,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
