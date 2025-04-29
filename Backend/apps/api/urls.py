from django.urls import path, include
from .views import get_rapports,top_genres, recommander_trajet, post_trajet, put_trajet, get_trajet, get_trajets

urlpatterns = [
    path('marketing/top-genres',top_genres, name='top-genres'),
    path('marketing/rapports', get_rapports, name='rapports'),
    path('recommandations/trajet/<int:trajetId>/', recommander_trajet, name='recommander-trajet'),
    path('trajets/<int:trajetId>/', get_trajet, name='get-trajet'),
    path('trajets/', get_trajets, name='get-trajets'),
    path('trajets/', post_trajet, name='post-trajet'),
    path('trajets/<int:trajetId>/', put_trajet, name='put-trajet'),
    
    
]
