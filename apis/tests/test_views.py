import pytest
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.test import APIClient

from apis.models import CustomUser
from apis.serializers import CustomUserSerializer
from apis.views import UserRegistrationAPIView, UserLoginAPIView


@pytest.mark.django_db
class TestUserViews:

    def test_user_registration_success(self, user_data, client):
        """Tests successful user registration."""
        data = user_data.copy()  # Avoid modifying original fixture
        del data['password2']  # Password2 not required for view

        response = client.post('/users/', data=data, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert CustomUser.objects.filter(email=user_data['email']).exists()

    def test_user_registration_missing_fields(self, user_data, client):
        """Tests validation error for missing required fields."""
        del user_data['email']
        response = client.post('/users/', data=user_data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'email' in response.data.get('errors', {})

    def test_user_registration_password_mismatch(self, user_data, client):
        """Tests validation error when password2 doesn't match."""
        data = user_data.copy()
        data['password2'] = 'different_password'
        response = client.post('/users/', data=data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'password' in response.data.get('errors', {})

    def test_user_login_success(self, user_data, client):
        """Tests successful user login."""
        user = CustomUser.objects.create_user(**user_data)
        user.set_password(user_data['password'])
        user.save()

        data = {'email': user_data['email'], 'password': user_data['password']}
        response = client.post('/login/', data=data, format='json')

        assert response.status_code == status.HTTP_200_OK
        assert 'refresh' in response.data
        assert 'access' in response.data

    def test_user_login_invalid_credentials(self, client):
        """Tests login error for invalid credentials."""
        data = {'email': 'invalid@example.com', 'password': 'wrong_password'}
        response = client.post('/login/', data=data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'error' in response.data

    def test_user_login_missing_fields(self, client):
        """Tests login error for missing required fields."""
        data = {'email': 'invalid@example.com'}
        response = client.post('/login/', data=data, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'password' in response.data.get('errors', {})
