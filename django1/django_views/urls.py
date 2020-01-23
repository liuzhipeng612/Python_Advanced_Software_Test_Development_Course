from django.urls import path

from django_views.views import HomeIndex
from .views import HomeIndex

urlpatterns = [
    path('index/', HomeIndex.as_view()),
]
