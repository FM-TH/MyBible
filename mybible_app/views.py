from dataclasses import field
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from .models import Book
from django.urls import reverse_lazy
import app_local
# import requests


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class MypageView(TemplateView):
    template_name = 'mypage.html'


class BibleCreate(CreateView):
    template_name = 'create.html'
    model = Book
    fields = ('book_title', 'author', 'keyword1',
              'keyword2', 'keyword3', 'comment')
    success_url = reverse_lazy('mypage')


class BiblesList(ListView):
    template_name = 'bibles.html'
    model = Book


def searchbooks(query):
    print("API entered")
    API_KEY = app_local.API_KEY_LOCAL
    endpoint = "https://www.googleapis.com/books/v1"
    url = endpoint + "/volumes?q=" + query
    # 検索機能どうやっていれるかフォームからこの関数に入れるには？
