from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

<<<<<<< Updated upstream
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username',)
=======

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username','first_name','is_staff')
>>>>>>> Stashed changes
