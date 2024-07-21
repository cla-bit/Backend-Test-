from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    """Product category Model fields"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Product Model fields"""
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
