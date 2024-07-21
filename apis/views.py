from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_205_RESET_CONTENT,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserRegistrationAPIView(ModelViewSet):
    """API endpoint for user registration."""
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserLoginAPIView(APIView):
    """API endpoint for user registration."""
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Username and password required'}, status=HTTP_400_BAD_REQUEST)
        user = authenticate(email=email, password=password)

        if not user:
            return Response({'error': 'Invalid credentials'}, status=HTTP_400_BAD_REQUEST)

        refresh_token = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(refresh_token),
                'access': str(refresh_token.access_token)
            }
        )


class UserLogoutAPIView(APIView):
    """API endpoint for user registration."""
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh_token']
            access_token = RefreshToken(refresh_token)
            access_token.blacklist()

            return Response({'message': 'Access token has been successfully blacklisted.'},
                            status=HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_400_BAD_REQUEST)
