from rest_framework import serializers
from .models import Test
from .models import Profession

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['text']

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ['id', 'nom_profession']