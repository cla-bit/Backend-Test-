""" Serialization of the Custom User model from the database"""

from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser model"""
    password = serializers.CharField(max_length=255, write_only=True)
    password2 = serializers.CharField(max_length=255, write_only=True)
    agreement = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password', 'password2', 'agreement')
        extra_kwargs = {'password': {'write_only': True, 'required': True},
                        'password2': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        """Create and return a new user"""
        custom_user = CustomUser.objects.create_user(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            agreement=self.validated_data['agreement'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        custom_user.set_password(password)
        custom_user.save()
        return custom_user
