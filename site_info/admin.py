from django.contrib import admin

from .models import Contact, About


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('full_name', 'subject', 'date', 'email')
    list_filter = ('subject', 'full_name')
    search_fields = ('full_name', 'subject', 'email')


@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    list_display = ('title', 'email', 'phone_number')
    list_filter = ('title',)
