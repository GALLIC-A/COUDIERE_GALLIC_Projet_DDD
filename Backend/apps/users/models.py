from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Ajoute ici tes champs personnalisés
    #avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    pass