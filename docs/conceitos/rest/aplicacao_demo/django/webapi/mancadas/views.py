from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


class IndividuoViewSet(viewsets.ModelViewSet):
    queryset = Individuo.objects.all()
    serializer_class = IndividuoSerializer


class MancadaViewSet(viewsets.ModelViewSet):
    queryset = Mancada.objects.all()
    serializer_class = MancadaSerializer
