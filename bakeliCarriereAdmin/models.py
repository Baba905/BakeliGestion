from django.db import models

class Eleve(models.Model):
    nom: models.CharField(max_length= 30)
    prenom: models.CharField(max_length= 30)
    annee: models.DateTimeField(auto_now=False)
    niveau: models.CharField(max_length=5)
