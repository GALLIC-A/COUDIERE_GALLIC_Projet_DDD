from django.db import models
from .managers import ProfessionManager

class Lieu(models.Model):
    nom = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.nom

class Profession(models.Model):
    nom_profession = models.CharField(max_length=255)

    # Il faut lier la classe métier à son manager (= repository)
    objects = ProfessionManager()

    def __str__(self):
        return self.nom_profession

class Traffic(models.Model):
    date = models.DateTimeField()
    valeur_traffic = models.FloatField()
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)

class Population(models.Model):
    date = models.DateTimeField()
    age_moyen = models.IntegerField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)

class Musique(models.Model):
    date = models.DateTimeField()
    genre = models.CharField(max_length=255)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)

class Test(models.Model):
    texte = models.CharField(max_length=10)