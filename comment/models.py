from django.db import models
from gig.models import Gig
from proFile.models import Profile
from django.contrib.auth import get_user_model


User = get_user_model()


class Comment(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE,null=True,verbose_name='گیگ')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,verbose_name='کاربر')
    content = models.TextField(max_length=400,verbose_name='متن پیام')
    publish = models.DateTimeField(auto_now_add=True,null=True,verbose_name='متن پیام')
    status = models.BooleanField(default=False,verbose_name='وضعیت')

    class Meta:
        ordering = ("-publish",)
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.user}'
