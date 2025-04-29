from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Role

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role=serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), allow_null=True, required=False)
    class Meta:
        model=User
        fields=['id','username','email','password', 'role']

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)