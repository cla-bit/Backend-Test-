""" Url paths"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView

app_name = 'api'

routers = DefaultRouter()
routers.register(r'register', UserRegistrationAPIView, basename='user')

urlpatterns = [
    path('auth/login/', UserLoginAPIView.as_view(), name='login'),
    path('auth/logout/', UserLogoutAPIView.as_view(), name='logout'),
    path('auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += routers.urls
