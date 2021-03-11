from django.contrib import admin
from .models import Comment


def approve_comments(modeladmin, request, queryset):
    number = queryset.update(status=True)
    if number == 1:
        message = 'یک پیام '
    else:
        message = '{} پیام '.format(number)
    modeladmin.message_user(request, '{}'.format(message))


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('gig', 'user', 'content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('content',)
    actions = ['approve_comments']
