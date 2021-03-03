from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'slug']
    search_fields = ['title', 'slug']
    
admin.site.register(Category , CategoryAdmin)