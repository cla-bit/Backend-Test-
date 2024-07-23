""" Serialization of the object from database"""
from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for the OrderItem model"""
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for the Order model"""
    items = OrderItemSerializer(many=True, write_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'created', 'updated']

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     order = Order.objects.create(**validated_data)
    #     for item_data in items_data:
    #         product = item_data['product']
    #         quantity = item_data['quantity']
    #         price = item_data['price']
    #         OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
    #     return order
    #
    # def update(self, instance, validated_data):
    #     items_data = validated_data.pop('items')
    #     instance.save()
    #
    #     # Delete old items
    #     instance.items.all().delete()
    #
    #     # Create new items
    #     for item_data in items_data:
    #         OrderItem.objects.create(order=instance, **item_data)
    #     return instance
