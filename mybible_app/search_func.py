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
    ProcessedData = []
    # 加工したデータをリストに格納
    for JsonObj in JsonData["items"]:
        ProcessedData.append(JsonObj["volumeInfo"])
    # title, authors, descriptionを取り出し
    for x in ProcessedData:
        authorExist = "authors" in x
        descriptionExist = "description" in x

        print(x["title"])
        if authorExist == True:
            print(x["authors"])
        else:
            print("著者は不明です")

        if descriptionExist == True:
            print(x["description"])
        else:
            print("説明はありません")
        print("**************************")
        print("\n")


searchbooks(query)
