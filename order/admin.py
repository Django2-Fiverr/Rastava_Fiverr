from django.contrib import admin

from order.models import Order, OrderDetail


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('owner', 'show_gigs', 'date_of_payment','get_total_price', 'paid')
    list_filter = ('paid',)
    search_fields = ('owner',)




@admin.register(OrderDetail)
class AdminOrderDetail(admin.ModelAdmin):
    list_display = ('order', 'price', 'gig', 'count')
    list_filter = ('order', 'gig')
    search_fields = ('order',)
