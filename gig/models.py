import os
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from datetime import date
from django.utils import timezone
from category.models import Category

# use the custom user table ( the default one in settings.py)
User = get_user_model()


# This function splits file name and its format ( one.jpg -> one + .jpg )
def split_name(file_name):
    base_name = os.path.basename(file_name)
    name, format = os.path.splitext(base_name)
    return name, format


# This function changes default file name and uses the same format ( one.jpg -> two.jpg )
# it returns an address to save the uploaded image file
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

   
    def grouping_gigs(self, slug):
        items = self.get_queryset().filter(category__name=slug)
        return items


class Gig(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='موضوع')
    slug = models.SlugField(max_length=20, blank=True, verbose_name='پیوست')
    cost = models.IntegerField(verbose_name='قیمت')
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

    # returns the name of the gig owner
    def __str__(self):
<<<<<<< HEAD
        return f'{self.user.username}-{self.title}'
=======
        return f'{self.title}'
>>>>>>> sajad

    def get_absolute_url(self):
        return f'/gigs/gig-detail/{self.id}/'





