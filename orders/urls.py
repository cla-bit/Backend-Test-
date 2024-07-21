""" Url paths"""

# from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet


app_name = 'orders'

routers = DefaultRouter()
routers.register('orders', OrderViewSet)

urlpatterns = routers.urls
