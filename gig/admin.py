from django.contrib import admin

from .models import Gig
# Register your models here.
# admin.site.register(User)

class GigAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category']
    
admin.site.register(Gig, GigAdmin)
