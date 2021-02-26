from django.contrib import admin
from . import models
from comment.models import Comments

@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('profile', 'user', 'content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')