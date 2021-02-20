from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Gig(models.Model):
    slug = models.SlugField(unique=True)
    cost = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sell_count = models.CharField(max_length=10,default='0')
    
