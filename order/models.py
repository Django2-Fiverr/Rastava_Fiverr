from django.db import models
from user.models import User
from django.utils import timezone
from gig.models import Gig
# Create your models here.


class Order(models.Model):
    CHOICES_ORDER = (
        ('A','Access'),
        ('N','Not Access'),
    )
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    gig = models.ForeignKey(Gig, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    price = models.CharField(max_length=10)
    thumbnail = models.ImageField(upload_to='images')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=CHOICES_ORDER)

    # def __str__(self):
    #     return self.gig

