from bakeliGestion import models
from bakeliGestion.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields =('url','username','email', 'user_type')

class EtablissementSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = models.Etablissement
        fields =('nom', 'adresse', 'user')

class EleveSerializer(serializers.HyperlinkedModelSerializer):
    etablissement = serializers.HyperlinkedRelatedField(view_name='etablissement-detail', many= False, read_only=True)
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = models.Eleve
        fields = ('nom','prenom', 'etablissement','niveau', 'user')


class EntrepriseSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = models.Entreprise
        fields = ('nom','adresse','numeroSiret','secteur', 'user')