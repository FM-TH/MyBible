import requests
from .app_local import API_KEY_LOCAL
import json


def searchbooks(query):
    print("API entered")
    API_KEY = API_KEY_LOCAL
    url = "https://www.googleapis.com/books/v1/volumes"
    payload = {"q": query, "key": API_KEY}
    # google books apiからいろんなデータ受け取る
    r = requests.get(url, params=payload)
    print(r.json)


searchbooks("鬼滅")
