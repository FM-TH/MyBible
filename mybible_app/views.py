from dataclasses import field
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from .models import Book
from django.urls import reverse_lazy
from .app_local import API_KEY_LOCAL
import requests


# Create your views here.

def searchbooks(request):
    print("API entered")
    API_KEY = API_KEY_LOCAL

    try:
        query = request.GET["q"]
    except KeyError:
        pass

    url = "https://www.googleapis.com/books/v1/volumes"

    try:
        payload = {"q": query, "key": API_KEY}
    except:
        payload = {"q": "ハンターハンター", "key": API_KEY}

    # google books apiからいろんなデータ受け取る
    r = requests.get(url, params=payload)
    JsonData = r.json()
    ProcessedData = []
    # 加工したデータをリストに格納
    for JsonObj in JsonData["items"]:
        ProcessedData.append(JsonObj["volumeInfo"])

    # リスト格納する辞書を用意
    context = {"BookTitle": [], "BookAuthor": [], "BookDescription": []}

    # title, authors, descriptionを取り出し
    for x in ProcessedData:
        authorExist = "authors" in x
        descriptionExist = "description" in x

        context["BookTitle"].append(x["title"])

        if authorExist == True:
            context["BookAuthor"].append(x["authors"])
        else:
            context["BookTitle"].append("著者は不明です")

        if descriptionExist == True:
            context["BookDescription"].append(x["description"])
        else:
            context["BookTitle"].append("説明はありません")

    # 動作確認
    for i in range(5):
        print(context["BookTitle"][i])
        print(context["BookAuthor"][i])
        print(context["BookDescription"][i])
        print("*******************")
        print("\n")
    return render(request, 'searchbooks.html')


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
