from django.db import models
from gig.models import Gig
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, related_name='gig')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    subject = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    content = models.TextField(max_length=150)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return f'Comment by {self.user}, Email:'