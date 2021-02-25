from django.contrib import admin
from proFile.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','birth','image')
    
admin.site.register(Profile, ProfileAdmin)
