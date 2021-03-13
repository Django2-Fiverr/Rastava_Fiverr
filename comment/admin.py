from django.contrib import admin
from .models import Comment


def approve_comments(modeladmin, request, queryset):
    number = queryset.update(status=True)
    if number == 1:
        message = 'یک مورد '
    else:
        message = '{} مورد '.format(number)
    modeladmin.message_user(request, '{} با موفقیت منتشر شدند.'.format(message))


def disable_comments(modeladmin, request, queryset):
    number = queryset.update(status=False)
    if number == 1:
        message = ' یک مورد'
    else:
        message = f'{number} مورد '
    modeladmin.message_user(request, f'{message} باموفقیت غیر فعال شدند ')


approve_comments.short_description = 'تغییر وضعیت به حالت انتشار'
disable_comments.short_description = 'تغییر وضعیت به حالت غیر فعال'


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('gig', 'user','reply_to', 'content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('content',)
    actions = [approve_comments,disable_comments]
