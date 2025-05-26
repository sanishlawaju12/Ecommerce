from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ('email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'phone', 'name','type', 'password')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions',)}),   #'is_customer' , 'is_seller'
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'phone', 'name', 'type', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)