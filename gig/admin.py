from django.contrib import admin
from .models import Comment
from gig.models import Gig


def make_available(modeladmin, request, queryset):
    number = queryset.update(active=True)
    if number == 1:
        result = 'یک گیگ '
    else:
        result = f'{number} گیگ '
    modeladmin.message_user(request, 'تعداد {}با موفقیت به حالت فعال تغییر داده شد'.format(result))


def make_unavailable(modeladmin, request, queryset):
    number = queryset.update(active=False)
    if number == 1:
        result = 'یک گیگ '
    else:
        result = f'{number} گیگ '
    modeladmin.message_user(request, 'تعداد {}با موفقیت به حالت غیر فعال تغییر داده شد'.format(result))


make_unavailable.short_description = 'تغییر وضعیت به حالت غیرفعال'
make_available.short_description = 'تغییر وضعیت به حالت فعال'


@admin.register(Gig)
class AdminGig(admin.ModelAdmin):
    list_display = ('title', 'id', 'category', 'user', 'create', 'cost', 'active')
    list_filter = ('create', 'active', 'user', 'category')
    ordering = ('-create','cost', 'active')
    search_fields = ('title', 'description', 'user')
    actions = [make_available,make_unavailable]


# comment section

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('gig', 'user', 'content', 'publish', 'status')
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')
