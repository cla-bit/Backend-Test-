from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError

from products.models import ProductCategory, Product


@pytest.mark.django_db
class TestProductModels:

    def test_create_product_category(self):
        """Tests successful creation of a product category."""
        category_name = "Electronics"
        category = ProductCategory.objects.create(name=category_name)
        category.refresh_from_db()

        assert category.name == category_name

    def test_create_product_with_valid_data(self):
        """Tests successful creation of a product with a category."""
        category = ProductCategory.objects.create(name="Test Category 1")
        product_name = "Laptop"
        product_price = float(1299)
        product_description = "A powerful laptop for everyday tasks."
        product = Product.objects.create(
            name=product_name, category=category, price=product_price, description=product_description
        )
        product.refresh_from_db()

        assert product.name == product_name
        assert product.category == category
        assert product.price == float(product_price)
        assert product.description == product_description

