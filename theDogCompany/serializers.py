from .models import Persona,Auto,Carnet
from rest_framework import serializers

# Serialzers, se encargan de realizar las transformaciones ecesarias para guardar o leer datos desde una BD
# se necesita uno por cada modelo en la BD

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id','nombre','apellidoPaterno','apellidoMaterno')

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ('id','modelo','marca','patente','anio','persona')


class CarnetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carnet
        fields = ('id','fechaVencimiento','numeroSerie','activo','persona')


