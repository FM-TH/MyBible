from django.urls import path
from .views import BiblesList, HomeView, MypageView, BibleCreate

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mypage/', MypageView.as_view(), name='mypage'),
    path('bibles/', BiblesList.as_view(), name='list'),
    path('create/', BibleCreate.as_view(), name='create'),
]
