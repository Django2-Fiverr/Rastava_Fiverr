from django.contrib import admin
from category.models import Category, Field

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'slug']
    search_fields = ['title', 'slug']
    
admin.site.register(Category , CategoryAdmin)

class FieldAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image']
    search_fields = ['title',]
    
admin.site.register(Field , FieldAdmin)