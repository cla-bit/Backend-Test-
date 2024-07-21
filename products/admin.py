from django.db import models
from django.contrib import admin

from .models import ProductCategory, Product

# Register your models here.


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description']
    list_filter = ['name', 'price']
