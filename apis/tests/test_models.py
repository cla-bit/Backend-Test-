import pytest
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import CustomUser
from .serializers import CustomUserSerializer  # Assuming your serializer exists


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

    def test_create_user_missing_required_fields(self, user_data):
        """Tests validation error when required fields are missing."""
        del user_data['username']  # Remove username for testing
        with pytest.raises(ValidationError) as excinfo:
            CustomUser.objects.create_user(**user_data)

        assert 'username' in str(excinfo.value)

    def test_create_user_non_unique_email(self, user_data):
        """Tests validation error when creating user with a duplicate email."""
        CustomUser.objects.create_user(**user_data)
        with pytest.raises(ValidationError) as excinfo:
            CustomUser.objects.create_user(**user_data)

        assert 'email' in str(excinfo.value)

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

    def test_user_list_endpoint(self, user_data, client):
        """Tests the user list endpoint using DRF."""
        CustomUser.objects.create_user(**user_data)
        url = reverse('customuser-list')  # Assuming list view is named 'customuser-list'

        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert CustomUserSerializer(CustomUser.objects.all(), many=True).data in response.data

    def test_user_detail_endpoint(self, user_data, client):
        """Tests the user detail endpoint using DRF."""
        user = CustomUser.objects.create_user(**user_data)
        url = reverse('customuser-detail', kwargs={'pk': user.pk})  # Assuming detail view is parameterized

        response = client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert CustomUserSerializer(user).data == response.data
