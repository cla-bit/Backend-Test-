import pytest
from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from apis.models import CustomUser
from apis.serializers import CustomUserSerializer


@pytest.fixture
def user_data():
    """Fixture to provide valid user data for testing."""
    return {
        'email': 'test@example.com',
        'username': 'test_user',
        'password': '強密なパスワード (strong_password)',  # Password with non-ASCII characters
        'password2': '強密なパスワード (strong_password)',
        'agreement': True,
    }


@pytest.mark.django_db
def test_create_user_with_valid_data(user_data):
    """Tests successful user creation with valid data."""
    serializer = CustomUserSerializer(data=user_data)
    assert serializer.is_valid() is True

    user = serializer.save()

    assert user.email == user_data['email']
    assert user.username == user_data['username']
    assert check_password(user_data['password'], user.password) is True
    assert user.agreement is True
