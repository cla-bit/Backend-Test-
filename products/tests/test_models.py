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

    def test_create_product_category_with_empty_name(self):
        """Tests validation error for empty product category name."""
        with pytest.raises(ValidationError) as excinfo:
            ProductCategory.objects.create(name="")

        assert 'name' in str(excinfo.value)

    def test_create_product_with_valid_data(self, category):
        """Tests successful creation of a product with a category."""
        product_name = "Laptop"
        product_price = 1299.99
        product_description = "A powerful laptop for everyday tasks."
        product = Product.objects.create(
            name=product_name, category=category, price=product_price, description=product_description
        )
        product.refresh_from_db()

        assert product.name == product_name
        assert product.category == category
        assert product.price == product_price
        assert product.description == product_description

    def test_create_product_with_missing_fields(self):
        """Tests validation error for missing required product fields."""
        with pytest.raises(ValidationError) as excinfo:
            Product.objects.create(name="")

        assert 'name' in str(excinfo.value)

    def test_create_product_with_invalid_price(self, category):
        """Tests validation error for invalid product price (non-decimal)."""
        with pytest.raises(ValidationError) as excinfo:
            Product.objects.create(name="Phone", category=category, price="invalid_price", description="A mobile phone.")

        assert 'price' in str(excinfo.value)
