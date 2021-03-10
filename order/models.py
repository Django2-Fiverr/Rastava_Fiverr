import datetime
from django.db import models
from django.contrib.auth import get_user_model

from gig.models import Gig

User = get_user_model()


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='خریدار')
    paid = models.BooleanField(default=False, verbose_name='پرداخت شده / نشده')
    date_of_payment = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید کاربر'
        verbose_name_plural = 'سبد های خرید کاربران'

    def __str__(self):
        return self.owner.username

    def show_gigs(self):
        names = list(map(str, self.orderdetail_set.all()[0:3]))
        return ' ,'.join(names)

    def get_total_price(self):
        summation = 0
        for item in self.orderdetail_set.all():
            summation += item.price
        return summation

    def convert_total_price(self):
        price = self.get_total_price()
        return format(price, ',.2f')

    def calculate_taxes(self):
        taxes = self.get_total_price() * 0.09
        return format(taxes, ',.2f')

    def get_total_payment_price(self):
        result = self.get_total_price() * 1.09 * 10
        return round(result, 2)

    def convert_total_payment_price(self):
        price = self.get_total_payment_price() / 10
        return format(price, ',.2f')

    get_total_price.short_description = 'قیمت کل سبد خرید'
    show_gigs.short_description = 'محتویات سبد خرید'


class OrderDetail(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, verbose_name='گیگ مرد نظر')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    price = models.PositiveIntegerField(verbose_name='قیمت گیگ')
    deadline = models.IntegerField(verbose_name='مهلت تحویل سفارش')

    class Meta:
        verbose_name = 'جزپیات محصول'
        verbose_name_plural = 'جزپیات محصولات'

    def __str__(self):
        return self.gig.title


class Transaction(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transaction', null=True, verbose_name='فروشنده')
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='خریدار')
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True, verbose_name='گیگ مورد معامله')
    expiration = models.BooleanField(default=False, verbose_name='منقضی شده / نشده')
    date_of_transaction = models.DateTimeField(verbose_name='زمان انجام معامله')
    deadline = models.DateTimeField(verbose_name='مهلت تحویل')

    def __str__(self):
        return f'{self.client}->{self.gig}'

    class Meta:
        verbose_name = 'معامله'
        verbose_name_plural = 'معاملات'

    def remaining_time(self):
        date = self.deadline.date()
        time = self.deadline.time()
        result = datetime.datetime.combine(date, time) - datetime.datetime.now()
        if result.days < 0:
            self.expiration = True
            self.save()
        return result.days
