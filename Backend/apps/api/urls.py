from django.urls import path, include
from .views import get_tests, search_profession

urlpatterns = [
    path('tests/', get_tests, name='get_tests'),
    path('search_profession/', search_profession, name='search_profession'),
]
