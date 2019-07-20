from rest_framework import serializers

from store.models import Product, ProductRequest


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'price')


class ProductRequestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ProductRequest
        fields = ('name', 'category', 'description', 'image', 'owner')
