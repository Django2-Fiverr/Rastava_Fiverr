from django.contrib import admin
from proFile.models import Profile
<<<<<<< HEAD
from user.models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','birth','image')
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(User)
=======


@admin.register(Profile)
class AdminProfile(admin.ModelAdmin):
    list_display = ('user', 'last_update')
    search_fields = ('user',)
>>>>>>> dev
