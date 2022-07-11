from dataclasses import field
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from .models import Book
from django.urls import reverse_lazy
# from app_local import API_KEY_LOCAL
import requests


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    # def searchbooks(query):
    #     print("API entered")
    #     API_KEY = API_KEY_LOCAL
    #     url = "https://www.googleapis.com/books/v1/volumes"
    #     payload = {"q": query, "key": API_KEY}
    #     # google books apiからいろんなデータ受け取る
    #     r = requests.get(url, params=payload)


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
