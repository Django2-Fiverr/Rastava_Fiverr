from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', default = None, null = True, blank = True, on_delete = models.CASCADE, related_name = 'children')
    slug = models.SlugField(max_length=50, unique = True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ('title',)

    def __str__(self):
        return self.title

class Skills(models.Model):
    name = models.CharField(max_length=30, verbose_name='مهارت')

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return self.name


class Field(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'media_root', null= True)
    content = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ('title',)

    def __str__(self):
        return self.title