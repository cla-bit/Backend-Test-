from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem

# Create your views here.


class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        return self.request.user.orders.all()

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)
        order_item = OrderItem.objects.create(
            order=order,
            product=serializer.validated_data['product'],
            quantity=serializer.validated_data['quantity'],
            price=serializer.validated_data['price']
        )
        order_item.save()
