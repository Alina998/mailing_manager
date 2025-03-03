from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'phone_number', 'user_country', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'user_country', 'user_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'user_country', 'user_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
