from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test, Profession, Traffic, Musique
from .serializers import ProfessionSerializer, TrafficSerializer, MusiqueSerializer
from django.db.models import Count
from rest_framework.status import HTTP_200_OK

@api_view(['GET'])
def get_rapports(request):
    date_debut=request.GET.get('date-debut')
    date_fin=request.GET.get('date-fin')

    # Traitement
    return Response({
        "rapport":"rapportMarketing",
        "dateDebut":date_debut,
        "dateFin":date_fin
    })

@api_view(['GET'])
def top_genres(request):
    stats=Musique.objects.values('genre').annotate(nombreEcoutes=Count('id')).order_by('-nombreEcoutes')
    results=[
        {
            'genre':item['genre'],
            'nombreEcoutes':item['nombreEcoutes']
        }
        for item in stats
    ]
    return Response(results,status=HTTP_200_OK)

@api_view(['GET'])
def recommander_trajet(request, trajetId):
    return Response({
        'playlistId':2,
        'musiques':[
            {
                'titre':'LE TITRE DE LA MUSIQUE',
                'artiste':'LARTISTE',
                'url':'https://'
            }
        ]
    })

@api_view(['POST'])
def post_trajet(request):
    return Response({
        'trajetId':2,
        'details':'POST TRAJET'
    })

@api_view(['PUT'])
def put_trajet(request, trajetId):
    return Response({
        'trajetId':3,
        'updatedDetails':'2025-04-23'
    })

@api_view(['GET'])
def get_trajet(request, trajetId):
    return Response({
        'trajetDetails':'details du trajet'
    })
    
@api_view(['GET'])
def get_trajets(request):
    return Response("liste des trajets mais je n'ai pas réussi à le faire")
