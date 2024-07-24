import pytest
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.text import slugify
from rest_framework import status
from rest_framework.test import APIClient

from apis.models import CustomUser
from apis.serializers import CustomUserSerializer  # Assuming your serializer exists


@pytest.fixture
def user_data():
    """Fixture to provide valid user data for testing."""
    return {
        'email': 'test@example.com',
        'username': 'test_user',  # Included due to REQUIRED_FIELDS
        'agreement': True,
    }


@pytest.mark.django_db
class TestCustomUser:

    def test_create_user(self, user_data):
        """Tests successful user creation with valid data."""
        user = CustomUser.objects.create_user(**user_data)
        user.refresh_from_db()  # Ensure data is persisted

        assert user.email == user_data['email']
        assert user.username == user_data['username']
        assert user.agreement is True

    def test_create_user_automatic_slug(self, user_data):
        """Tests automatic slug generation from username."""
        user = CustomUser.objects.create_user(**user_data)
        user.refresh_from_db()

        assert user.slug == slugify(user_data['username'])

    def test_user_str_representation(self, user_data):
        """Tests the __str__ method returns the user's email."""
        user = CustomUser.objects.create_user(**user_data)
        user.refresh_from_db()

        assert str(user) == user.email
