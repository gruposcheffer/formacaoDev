from rest_framework import serializers
from .models import *


class IndividuoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individuo
        fields = '__all__'


class MancadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mancada
        fields = '__all__'
