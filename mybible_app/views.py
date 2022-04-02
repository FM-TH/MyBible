from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book

# Create your views here.


def HomeView(request):
    return render(request, "home.html")


class BiblesList(ListView):
    template_name = 'bibles.html'
    model = Book
