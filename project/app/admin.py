from .models import (UserAccount,
                     UserProfile,
                     UserRelationship)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AdminUser


class UserAdmin(AdminUser):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'type',
    )



    fieldsets = (
        (None, {
            'fields': ('username', 'password',)
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions',
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined',)
        }),
        ('Additional info', {
            'fields': ('type',)
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2',)
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions',
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined',)
        }),
        ('Additional info', {
            'fields': ('type', )
        })
    )


admin.site.register(UserAccount, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(UserRelationship)