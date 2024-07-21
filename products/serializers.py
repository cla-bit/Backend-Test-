""" Serialization of the object from the database"""
from rest_framework import serializers
from .models import ProductCategory, Product


class ProductCategorySerializer(serializers.ModelSerializer):
    """Serializer for the ProductCategory model"""
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for the Product model"""
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class DetailProductSerializer(ProductSerializer):
    category = ProductCategorySerializer()
