""" Url pahts"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationAPIView, ProductListView, ProductDetailViewSet

app_name = 'api'

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register('products', ProductViewSet)
# router.register('categories', ProductCategoryViewSet)

urlpatterns = [
    path('auth/register/', UserRegistrationAPIView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailViewSet.as_view(), name='product-detail'),  # noqa: E501
]

# urlpatterns += router.urls
