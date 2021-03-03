from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('gig', 'user', 'content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('content',)

