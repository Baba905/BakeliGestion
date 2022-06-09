from django.db import models
from eleve.models import Eleve
class Etablissement(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    eleves = models.ManyToManyField(Eleve)
