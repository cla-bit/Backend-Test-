# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS

from .models import ProductCategory, Product
from .serializers import ProductSerializer, ProductCategorySerializer, DetailProductSerializer

# Create your views here.


class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class ProductCategoryViewSet(ModelViewSet):
    """API endpoint for managing product categories."""
    permission_classes = [IsAdminOrReadOnly]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductViewSet(ModelViewSet):
    """API endpoint for managing products."""
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailProductSerializer
        return super().get_serializer_class()
