from django.db import models

class Etablissement(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nom     

class Offre(models.Model):
    titre= models.CharField(max_length=255)
    date= models.DateTimeField()
    details = models.TextField()

    def __str__(self) -> str:
        return self.titre
    

class Eleve(models.Model):
    nom = models.CharField(max_length= 30)
    prenom = models.CharField(max_length= 30)
    annee = models.DateTimeField()
    niveau = models.CharField(max_length=10)
    etablissement= models.ForeignKey('Etablissement', on_delete=models.CASCADE)
    offre = models.ManyToManyField('Offre', through='Postuler', through_fields=('eleve', 'offre'))

    def __str__(self) -> str:
        return self.nom   


class Entreprise(models.Model):
    nom =models.CharField(max_length=255)
    adresse= models.CharField(max_length=255)
    numeroSiret = models.IntegerField()
    secteur= models.CharField(max_length=255)
    offre= models.ForeignKey('Offre', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom   


class Postuler(models.Model):
    eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE )
    offre = models.ForeignKey('Offre', on_delete= models.CASCADE)



    