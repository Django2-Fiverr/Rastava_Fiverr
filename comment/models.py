from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from proFile.models import Profile

User = get_user_model()


class Comments(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='commentProfile')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentUser')
    name = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=30)
    content = models.TextField(max_length=150)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta:
        ordering = ("publish",)
    
    def __str__(self):
        return f'Comment by {self.name}, Email : {self.email}'