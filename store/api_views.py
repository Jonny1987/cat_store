from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from store.models import Product
from store.serializers import ProductSerializer


class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_lmit = 100


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProductSerializer
    filter_fields = ('id',)
    pagination_class = ProductPagination
