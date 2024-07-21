from django.db import models
from products.models import Product
from apis.models import CustomUser

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Order ID: {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
