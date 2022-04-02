from django.urls import path
from .views import BiblesList, HomeView

urlpatterns = [
    path('', HomeView),
    path('bibles', BiblesList.as_view()),
]
