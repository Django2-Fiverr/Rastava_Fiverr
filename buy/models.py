from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from gig.models import Gig
# Create your models here.

class Buy(models.Model):
    CHOICES_BUY = (
        ('P','Providing Service'),
        ('E','End Of Service Provider'),
    )
    buyid = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    gig = models.ForeignKey('Gig', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    price = models.CharField(max_length=10)
    thumbnail = models.ImageField(upload_to='images')
    buydate = models.DateTimeField(default=timezone.now)
    enddate = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1, choices=CHOICES_BUY)
