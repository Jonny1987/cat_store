from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from store.models import Product, ProductRequest
from store.serializers import ProductSerializer, ProductRequestSerializer
from store.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        IsAdminOrReadOnly,
    ]
    serializer_class = ProductSerializer
    filter_fields = ('id',)


class ProductRequestViewSet(viewsets.ModelViewSet):
    queryset = ProductRequest.objects.all()
    serializer_class = ProductRequestSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
