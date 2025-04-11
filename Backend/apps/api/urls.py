from django.urls import path, include
from .views import get_tests

urlpatterns = [
    path('tests/', get_tests, name='get_tests'),
]
