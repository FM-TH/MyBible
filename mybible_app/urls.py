from django.urls import path
from .views import BiblesList, MypageView, BibleCreate
from . import views

urlpatterns = [
    path('', views.searchbooks, name='searchbook'),
    path('mypage/', MypageView.as_view(), name='mypage'),
    path('bibles/', BiblesList.as_view(), name='list'),
    path('create/', BibleCreate.as_view(), name='create'),
]
