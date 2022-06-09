from django.db import models

class Entreprise(models.Model):

    nom =models.CharField(max_length=255)
    adresse= models.CharField(max_length=255)
    numeroSiret = models.IntegerField()
    secteur= models.CharField(max_length=255)