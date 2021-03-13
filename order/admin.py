from django.contrib import admin

from order.models import Order, OrderDetail, Transaction


class InlineOrderDetail(admin.TabularInline):
    model = OrderDetail


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('owner', 'show_gigs', 'date_of_payment', 'get_total_price', 'paid')
    list_filter = ('paid',)
    search_fields = ('owner',)
    inlines = [InlineOrderDetail]


@admin.register(OrderDetail)
class AdminOrderDetail(admin.ModelAdmin):
    list_display = ('order', 'gig','get_cost')
    list_filter = ('order', 'gig')
    search_fields = ('order',)


@admin.register(Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display = ('seller', 'client', 'gig', 'deadline', 'expiration', 'delivery_status')
    list_filter = ('seller', 'client', 'gig')
    search_fields = ('gig', 'client', 'seller')
