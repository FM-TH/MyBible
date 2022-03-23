from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Book

# Create your views here.


class BiblesList(ListView):
    template_name = 'bibles.html'
    model = Book
