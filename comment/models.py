from django.db import models
from gig.models import Gig
from proFile.models import Profile
from django.contrib.auth import get_user_model
from Fiverr import settings
from django.urls import reverse

User = get_user_model()

class Comment(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, related_name='comment_gig')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    subject = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    content = models.TextField(max_length=150)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return f'Comment by {self.user}'

    def get_absolute_url(self):
        return reverse('gig:delete_comment', kwargs={'id': self.id})
