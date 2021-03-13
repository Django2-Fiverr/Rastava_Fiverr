from django.db import models

from proFile.models import Profile
from extensions.mainObjects import User
from gig.models import Gig


class Comment(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True, verbose_name='گیگ')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='کاربر')
    content = models.TextField(max_length=400, verbose_name='متن پیام')
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='پاسخ')
    create = models.DateTimeField(null=True,verbose_name='تاریخ ایجاد')
    publish = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ انتشار')
    status = models.BooleanField(default=False, verbose_name='وضعیت انتشار')

    class Meta:
        ordering = ("-publish",)
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return f'{self.user}'

    def get_date(self):
        return self.create.date().__str__()

    def get_time(self):
        return self.create.time().__str__()[:8]
