from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(BaseUserAdmin):
    # add user form field
    add_fieldsets = (
        (None, {
            'fields': ('email', 'username', 'is_student', 'is_teacher', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    # once the user is created this will show
    fieldsets = (
        (None, {
            "fields": ('email', 'username', 'is_student', 'is_teacher', 'password'),
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    list_display = ['email', 'username', 'is_student', 'is_teacher']
    search_field = ('email', 'username')
    ordering = ('email',)
    

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
