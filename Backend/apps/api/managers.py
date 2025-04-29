# En Django, les "managers" sont visiblement des équivalent des "repositories" que nous connaissons en Spring ou en Symfony.
from django.db import models 

class ProfessionManager(models.Manager):
    def find_by_name(self, name):
        return self.filter(nom_profession__icontains=name)