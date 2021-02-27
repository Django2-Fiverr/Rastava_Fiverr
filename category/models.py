from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, help_text='Write a topic ex:photo edit, programming,...')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوع ها'
