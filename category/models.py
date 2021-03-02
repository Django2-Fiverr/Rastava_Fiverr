from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)
    parent = models.ForeignKey('self', default = None, null = True, blank = True, on_delete = models.CASCADE, related_name = 'children')
    slug = models.SlugField(max_length=50, unique = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
