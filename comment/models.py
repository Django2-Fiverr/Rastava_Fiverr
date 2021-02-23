from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from gig.models import Gig

class Comments(models.Model):
    text = models.TextField(
        max_length=300, help_text='Write Your comment here')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    gig = models.ForeignKey('Gig', on_delete=models.SET_NULL, null=True)