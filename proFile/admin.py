from django.contrib import admin
from proFile.models import Profile


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'last_update','show_skills','image')
    search_fields = ('user','show_skills')
