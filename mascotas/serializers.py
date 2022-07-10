from rest_framework import serializers
from .models import mascota
from .models import producto

class mascotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = mascota
        fields = ('raza', 'peso', 'estatura', 'annos_de_vida', 'precio')

class productoSerializer(serializers.ModelSerializer):

    class Meta:
        model = producto
        fields = ('codigo', 'nombre', 'cantidad', 'precio')
