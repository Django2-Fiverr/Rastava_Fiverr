from django.contrib import admin
from .models import Category
from mptt.admin import MPTTModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]
    
admin.site.register(Category , MPTTModelAdmin)