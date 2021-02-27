from django.contrib import admin
from proFile.models import Profile
from user.models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','birth','image')
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(User)
