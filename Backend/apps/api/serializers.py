from rest_framework import serializers
from .models import Test, Profession, Lieu, Traffic, Musique

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['text']

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'nom_profession']

class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = ['id', 'nom', 'lat', 'lon']

class TrafficSerializer(serializers.ModelSerializer):
    lieu = LieuSerializer()
    
    class Meta:
        model = Traffic
        fields = ['id', 'date', 'valeur_traffic', 'lieu']

class MusiqueSerializer(serializers.ModelSerializer):
    lieu = LieuSerializer()

    class Meta:
        model = Musique
        fields = ['id', 'date', 'genre', 'lieu']