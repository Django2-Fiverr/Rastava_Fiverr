from django.contrib import admin
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']
    search_fields = ['name', 'subject', 'message']
    
admin.site.register(Contact , ContactAdmin)
