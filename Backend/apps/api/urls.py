from django.urls import path, include
from .views import get_tests, search_profession, get_traffic, get_musique

urlpatterns = [
    path('tests/', get_tests, name='get_tests'),
    path('profession/', search_profession, name='search_profession'),
    path('traffic/', get_traffic, name='get_traffic'),
    path('musique/', get_musique, name='get_musique'),
]
