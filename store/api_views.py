from rest_framework import viewsets, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from store.models import Product, ProductRequest
from store.serializers import ProductSerializer, ProductRequestSerializer
from store.permissions import IsOwnerOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProductSerializer
    filter_fields = ('id',)


class ProductRequestList(ListCreateAPIView):
    queryset = ProductRequest.objects.all()
    serializer_class = ProductRequestSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def perform_create(serializer):
        serializer.save(owner=self.request.user)


class ProductRequestDetail(RetrieveUpdateDestroyAPIView):
    queryset = ProductRequest.objects.all()
    serializer_class = ProductRequestSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]
