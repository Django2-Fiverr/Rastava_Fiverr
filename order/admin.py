from django.contrib import admin

from order.models import Order, OrderDetail, Transaction


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('owner', 'show_gigs', 'date_of_payment', 'get_total_price', 'paid')
    list_filter = ('paid',)
    search_fields = ('owner',)


@admin.register(OrderDetail)
class AdminOrderDetail(admin.ModelAdmin):
    list_display = ('order', 'price', 'gig')
    list_filter = ('order', 'gig')
    search_fields = ('order',)


@admin.register(Transaction)
class AdminOrderDetail(admin.ModelAdmin):
    list_display = ('seller', 'client', 'gig', 'deadline','expiration')
    list_filter = ('seller', 'client', 'gig')
    search_fields = ('gig', 'client', 'seller')
