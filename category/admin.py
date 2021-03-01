from django.contrib import admin

from category.models import Category, Skills


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Skills)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
