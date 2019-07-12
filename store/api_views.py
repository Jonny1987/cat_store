from rest_framework import viewsets, permissions

from store.models import Product
from store.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProductSerializer
    filter_fields = ('id',)
