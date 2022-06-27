from rest_framework import serializers
from .models import mascota

class mascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = mascota
        fields = ('raza', 'peso', 'estatura', 'annos_de_vida', 'precio')

