from dataclasses import field
from bakeliGestion.models import Eleve
from rest_framework import serializers

class ELeveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleve
        field= [' nom','prenom', 'niveau']