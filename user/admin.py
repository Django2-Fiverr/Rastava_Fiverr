from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username','first_name','is_staff')
