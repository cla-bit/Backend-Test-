from django_filters import FilterSet
from .models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'icontains'],
            'category__name': ['exact', 'icontains'],
            'price': ['gte', 'lte'],
        }
