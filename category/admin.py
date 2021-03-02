from django.contrib import admin
from category.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'slug']
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Category , CategoryAdmin)