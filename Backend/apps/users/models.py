from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.role_name

class CustomUser(AbstractUser):
    #avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    #pass
    role=models.ForeignKey(Role,on_delete=models.SET_NULL,null=True,blank=True,related_name="users")