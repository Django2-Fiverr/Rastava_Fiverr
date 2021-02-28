from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.Foreignkey('self', default = None, Null = True, blank = True, on_delete = models.CASCADE, related_name = 'children')
    slug = models.SlugField(max_length=255, unique = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
