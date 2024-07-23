""" Url paths"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderAPIView, OrderHistoryView


app_name = 'orders'

urlpatterns = [
    path('orders/', OrderAPIView.as_view(), name='order'),
    path('history/', OrderHistoryView.as_view(), name='history')  # Add endpoint for order history
]
