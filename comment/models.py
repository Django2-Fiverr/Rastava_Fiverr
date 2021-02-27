from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from proFile.models import Profile

User = get_user_model()

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='commentProfile')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentUser')
    name = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=30)
    comment = models.TextField(max_length=150)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    class Meta:
        ordering = ("publish",)
    
    def __str__(self):
        return f'Comment by {self.name}, Email : {self.email}'         

class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="recomment")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    re_comment = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment.id},{self.comment.title}"
