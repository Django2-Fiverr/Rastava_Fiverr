from django.db import models

<<<<<<< HEAD
class Category(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', default = None, null = True, blank = True, on_delete = models.CASCADE, related_name = 'children')
    slug = models.SlugField(max_length=50, unique = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
=======

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
>>>>>>> dev
