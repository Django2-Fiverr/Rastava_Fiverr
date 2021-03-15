from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('gig', 'reply', 'user', 'content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('content',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(status=True)
    

