from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from category.models import Category

class Gig(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, help_text='The owner of service')
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title}'