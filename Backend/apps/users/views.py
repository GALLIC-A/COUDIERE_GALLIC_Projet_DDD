from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({
                'message':'Utilisateur créé avec succès',
                'user':serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method=='POST':
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']

            user=authenticate(username=username, password=password)

            if user:
                refresh=RefreshToken.for_user(user)
                return Response({
                    'message':'Connexion réussie',
                    'access_token':str(refresh.access_token),
                    'refresh_token':str(refresh)
                }, status=status.HTTP_200_OK)
            return Response({'message':'Identifiants incorrects'},status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
