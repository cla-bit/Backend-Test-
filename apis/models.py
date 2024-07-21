"""Create and manage core app models."""

from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    slug = models.SlugField(unique=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), null=True, blank=True, max_length=100)
    agreement = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'agreement']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)  # Automatically create slug from username
        super().save(*args, **kwargs)



# class UserManager(BaseUserManager):
#     """USER MANAGER CLASS GOING TO MANAGE OUR USER CLASS."""
#
#     def create_user(self, email, password=None, **extra_fields):
#         """Create_user method creates and saves new user objects."""
#         if not email:
#             raise ValueError('User must have valid email address')
#
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, password):
#         """Create and saves a new super user."""
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#
#         return user
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     """Custom user model that supports using email instead of username."""
#
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
