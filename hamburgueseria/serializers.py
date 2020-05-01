from rest_framework import serializers
from .models import Ingrediente, Hamburguesa

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')

        def create(self, validated_data):
            return Ingrediente.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.nombre = validated_data.get('nombre', instance.nombre)
            instance.descripcion = validated_data.get('descripcion', instance.descripcion)
            return instance


class HamburguesaSerializer(serializers.ModelSerializer):
    ingredientes_hamburguesa = IngredienteSerializer(read_only=True, many=True)
    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'precio', 'descripcion', 'imagen', 'ingredientes_hamburguesa')

        def create(self, validated_data):
            return Hamburguesa.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.nombre = validated_data.get('nombre', instance.nombre)
            instance.precio = validated_data.get('precio', instance.precio)
            instance.descripcion = validated_data.get('descripcion', instance.descripcion)
            instance.imagen = validated_data.get('imagen', instance.imagen)

            return instance

