from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from .serializers import OrderSerializer, OrderItemSerializer
from .models import Order, OrderItem
from products.models import Product

# Create your views here.


class OrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """ Get user and product data from request"""
        user = request.user
        product_data = request.data.get('products')

        if not product_data:
            return Response({'products': 'This field is required.'}, status=HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=user)
        for product in product_data:
            product_id = product.get('id')
            quantity = product.get('quantity')
            price = product.get('price')

            if not product_id or quantity <= 0:
                return Response({'products': 'This field is required.'}, status=HTTP_400_BAD_REQUEST)

            product_item = get_object_or_404(Product, pk=product_id)
            OrderItem.objects.create(order=order, product=product_item, quantity=quantity, price=price)

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=HTTP_201_CREATED)


class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


# class OrderViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()
#
#     def get_queryset(self):
#         return self.request.user.orders.all()
#
#     def perform_create(self, serializer):
#         order = serializer.save(user=self.request.user)
#         order_item = OrderItem.objects.create(
#             order=order,
#             product=serializer.validated_data['product'],
#             quantity=serializer.validated_data['quantity'],
#             price=serializer.validated_data['price']
#         )
#         order_item.save()
