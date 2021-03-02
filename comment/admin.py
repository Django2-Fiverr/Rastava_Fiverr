from django.contrib import admin
from . import models
from comment.models import Comment

@admin.register(models.Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('gig', 'user', 'content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')