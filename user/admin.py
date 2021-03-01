from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'date_joined','is_staff','is_anonymous')
    list_filter = ('date_joined',)
    search_fields = ('first_name', 'last_name', 'email', 'username', 'phone_number')
