from django.contrib import admin

from category.models import Category, Skills, Field


class FieldsInline(admin.TabularInline):
    model = Field


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [FieldsInline,]


@admin.register(Skills)
class AdminSkills(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Field)
class AdminField(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('category', 'title')
