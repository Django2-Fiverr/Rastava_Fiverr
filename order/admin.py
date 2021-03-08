from django.contrib import admin

from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('gig',)}
    list_display = ['gig', 'slug', 'description', 'price', 'status']
admin.site.register(Order, OrderAdmin)

