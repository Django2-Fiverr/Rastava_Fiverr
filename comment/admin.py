from django.contrib import admin
from .models import Comment,ReplyComment,Post

class CommentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'user', 'content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')
admin.site.register(Comments)

class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 're_comment', 'time')
admin.site.register(ReplyComment)
