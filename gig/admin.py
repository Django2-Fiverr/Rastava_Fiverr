from django.contrib import admin

from gig.models import Gig


@admin.register(Gig)
class AdminGig(admin.ModelAdmin):
    list_display = ('id', 'category', 'user', 'create', 'cost', 'active')
