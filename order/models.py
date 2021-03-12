import datetime

from django.db import models

from gig.models import Gig

from extensions.mainObjects import User
from extensions.functions import re_format_price
from extensions.functions import split_name
from extensions.functions import remaining_time
from extensions.functions import get_total_price


# This function changes default file name and uses the same format ( one.jpg -> two.jpg )
# it returns an address to save the uploaded image file
def get_name(instance, file_name):
    name, ext = split_name(file_name)
    current_time = datetime.date.today()
    new_name = '{}-{}-{}{}'.format(str(current_time), instance.gig.title, instance.client, ext)
    return 'transaction/{}/{}'.format(instance.seller, new_name)


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
        return get_total_price(self)

    def convert_total_price(self):
        price = self.get_total_price()
        return re_format_price(price)

    def calculate_taxes(self):
        taxes = self.get_total_price() * 0.09
        return re_format_price(int(taxes))

    def get_total_payment_price(self):
        result = self.get_total_price() * 1.09 * 10
        return round(result, 2)

    def convert_total_payment_price(self):
        price = self.get_total_price()
        return re_format_price(price)

    convert_total_payment_price.short_description = 'قیمت کل سبد خرید'
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
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, verbose_name='فروشنده')
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='خریدار')
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True, verbose_name='گیگ مورد معامله')
    expiration = models.BooleanField(default=False, verbose_name='منقضی شده / نشده')
    delivery_status = models.BooleanField(default=False, verbose_name='وضعیت/ تحویل')
    date_of_transaction = models.DateTimeField(verbose_name='زمان انجام معامله')
    deadline = models.DateTimeField(verbose_name='مهلت تحویل')
    file = models.FileField(upload_to=get_name, blank=True, null=True, verbose_name='فایل ارسالی')

    def __str__(self):
        return f'{self.client}->{self.gig}'

    class Meta:
        verbose_name = 'معامله'
        verbose_name_plural = 'معاملات'

    def remaining_time(self):
        return remaining_time(self)
