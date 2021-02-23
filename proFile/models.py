from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from category.models import Category

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=1000, help_text='User bio')
    skills = models.ManyToManyField('Category', help_text='Choose Your Skills')
    birth = models.DateField('Birth', null=True, blank=True)