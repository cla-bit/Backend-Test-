""" URL Paths"""

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductCategoryViewSet


app_name = 'products'

routers = DefaultRouter()
routers.register('categories', ProductCategoryViewSet)
routers.register('products', ProductViewSet)

urlpatterns = routers.urls
