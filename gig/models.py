from django.db import models

from extensions.functions import re_format_price, split_name
from extensions.mainObjects import User
from django.db.models import Q
from datetime import date

from category.models import Category, Field


def get_name(instance, file_name):
    name, ext = split_name(file_name)
    current_time = str(date.today())
    new_name = '{}/{}/{}{}'.format(current_time, instance.user.username, instance.title, ext)
    return 'gigs/{}'.format(new_name)


# Gis manager class which customizes gig objects methods
class GigManager(models.Manager):
    def get_active_gigs(self):
        return self.get_queryset().filter(active=True)  # returns active ( available gigs )

    def get_by_id(self, pk):
        result = self.get_queryset().filter(id=pk)
        if result:
            return result.first()
        return None

    def search(self, query):
        lock_up = Q(title__icontains=query) | Q(description__icontains=query)
        return self.get_queryset().filter(lock_up, active=True).distinct()

    def grouping_gigs(self, title):
        items = self.get_queryset().filter(field__title=title)
        return items


class Gig(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, verbose_name='پست')
    slug = models.SlugField(max_length=20, blank=True, verbose_name='پیوست')
    cost = models.PositiveIntegerField(verbose_name='قیمت')
    description = models.TextField(max_length=5000, verbose_name='توضیحات')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='کاربر')
    sell_count = models.IntegerField(default=0, verbose_name='تعداد دفعات فروش')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    image = models.ImageField(upload_to=get_name, null=True, blank=True, verbose_name='تصویر')
    create = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')

    objects = GigManager()  # the previous class (Gig manager)

    class Meta:
        verbose_name = 'گیگ'
        verbose_name_plural = 'گیگ ها'
        ordering = ('-create',)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/gigs/gig-detail/{self.id}/'

    def re_format_cost(self):
        return re_format_price(self.cost)
