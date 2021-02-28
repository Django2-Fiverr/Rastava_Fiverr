from django.contrib import admin
from .models import Category, Post
from mptt.admin import MPTTModelAdmin

class PostAdmin(admin.ModelAdmin):
     list_display = ['title', 'category', 'content', 'slug']
     
admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    
admin.site.register(Category , MPTTModelAdmin)