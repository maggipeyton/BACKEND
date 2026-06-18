from rest_framework import viewsets
from producto.models import Producto
from producto.api.serializers import ProductoSerialize

class ProductoVewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerialize