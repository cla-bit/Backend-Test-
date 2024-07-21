from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group

from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ['-date_joined']
    list_display = ['email', 'username', 'slug', 'first_name', 'last_name',
                    'agreement', 'is_active', 'is_staff', 'is_superuser', 'last_login']
    search_fields = ['email', 'username']
    fieldsets = (
        (None, {'fields': ('email', 'slug', 'agreement', 'username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'slug',
                       'password', 'password2', 'groups', 'user_permissions',
                       'agreement', 'is_staff', 'is_active'),
        }),
    )
    prepopulated_fields = {"slug": ("username",)}
