from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'etablisssement'),
      (2, 'eleve'),
      (3, 'entreprise'),
  )
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)



class Etablissement(models.Model):
    user = models.OneToOneField('User', on_delete= models.CASCADE)
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nom

class Offre(models.Model):
    titre= models.CharField(max_length=255)
    date= models.DateField(auto_now_add=True)
    details = models.TextField()
    entreprise = models.ForeignKey('Entreprise', on_delete= models.CASCADE)
    def __str__(self) -> str:
        return self.titre
    

class Eleve(models.Model):
    user = models.OneToOneField('User', on_delete= models.CASCADE)
    nom = models.CharField(max_length= 30)
    prenom = models.CharField(max_length= 30)
    niveau = models.CharField(max_length=10)
    etablissement= models.ForeignKey('Etablissement', on_delete=models.CASCADE)
    offre = models.ManyToManyField('Offre', through='Postuler', through_fields=('eleve', 'offre'))

    def __str__(self) -> str:
        return self.nom   


class Entreprise(models.Model):
    user = models.OneToOneField('User', on_delete= models.CASCADE)
    nom =models.CharField(max_length=255)
    adresse= models.CharField(max_length=255)
    numeroSiret = models.IntegerField()
    secteur= models.CharField(max_length=255)
   

    def __str__(self) -> str:
        return self.nom   


class Postuler(models.Model):
    eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE )
    offre = models.ForeignKey('Offre', on_delete= models.CASCADE)



    