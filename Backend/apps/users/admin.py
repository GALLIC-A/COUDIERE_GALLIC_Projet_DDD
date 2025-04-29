from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Role

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active', 'role']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name']

admin.site.register(Role, RoleAdmin)
