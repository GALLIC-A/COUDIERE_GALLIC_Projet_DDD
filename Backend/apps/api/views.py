from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test, Profession, Traffic, Musique, Lieu
from .serializers import ProfessionSerializer, TrafficSerializer, MusiqueSerializer
from django.db.models import Count
from rest_framework.status import HTTP_200_OK
from django.db import connection

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
    date_debut=request.GET.get('date-debut')
    date_fin=request.GET.get('date-fin')

    with connection.cursor() as cursor:
        query="""
               SELECT api_musique.genre,api_lieu.nom,COUNT(api_musique.id) AS nombre
               FROM api_musique
               INNER JOIN api_lieu ON api_musique.lieu_id=api_lieu.id
               WHERE api_lieu.id = %s
        """
        params=[trajetId]
        if date_debut and date_fin:
            query+=" AND api_musique.date BETWEEN %s AND %s"
            params.extend([date_debut,date_fin])
        query+="""
            GROUP BY api_musique.genre,api_lieu.nom
            ORDER BY nombre DESC
        """
        cursor.execute(query,params)
        rows=cursor.fetchall()
    results=[
        {
            'genre':genre,
            'lieu':nom_lieu,
            'nombre':nombre
        }
        for (genre,nom_lieu,nombre) in rows
    ]
    if not results:
        results=[{
            'titre':'tout',
            'lieu':'Inconnu',
            'nombre':0
        }]
    return Response(results)        

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
