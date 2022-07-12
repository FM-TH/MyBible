import requests
from .app_local import API_KEY_LOCAL


def searchbooks(query):
    print("API entered")
    API_KEY = API_KEY_LOCAL
    url = "https://www.googleapis.com/books/v1/volumes"
    payload = {"q": query, "key": API_KEY}
    # google books apiからいろんなデータ受け取る
    r = requests.get(url, params=payload)
    JsonData = r.json()
    # print(JsonData["items"])
    ProcessedData = []
    for JsonObj in JsonData["items"]:
        # 加工したデータをリストに追加


searchbooks("夏目漱石")
