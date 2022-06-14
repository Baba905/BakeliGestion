from django.shortcuts import render
from bakeliGestion.models import Eleve
from bakeliGestion.serializers import ELeveSerializer
from rest_framework import viewsets


class EleveViewSet(viewsets.ModelViewSet):
    queryset = Eleve.objects.all().order_by('id')
    serializer_class = ELeveSerializer

