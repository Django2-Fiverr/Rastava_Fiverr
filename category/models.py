import os

from django.db import models


def split_name(file_name):
    base_name = os.path.basename(file_name)
    name, ext = os.path.splitext(base_name)
    return name, ext


def get_name(instance, file_name):
    name, ext = split_name(file_name)
    new_name = '{}/{}{}'.format(instance.category.name, instance.title, ext)
    return 'category/{}'.format(new_name)


class Category(models.Model):
    name = models.CharField(max_length=20, help_text='Write a topic ex:photo edit, programming,...')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوع ها'


class Skills(models.Model):
    name = models.CharField(max_length=30, verbose_name='مهارت')

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return self.name


class Field(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='عنوان')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='موضوع')
    image = models.ImageField(upload_to=get_name, blank=True, null=True, verbose_name='تصویر')
    content = models.TextField(max_length=300, verbose_name='توضیحات', null=True, blank=True)

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ('title',)

    def __str__(self):
        return self.title
