from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .signup import CustomUserCreationForm
from .models import signupUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = signupUser
    list_display = ['username', 'number', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('number',)}),
    )
admin.site.register(signupUser, CustomUserAdmin)