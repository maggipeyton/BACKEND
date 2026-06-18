from rest_framework import serializers
from producto.models import Producto


class ProductoSerialize(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'