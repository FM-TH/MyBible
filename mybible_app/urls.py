from django.urls import path
from .views import BiblesList

urlpatterns = [
    path('bibles', BiblesList.as_view()),
]
