from django.db import models
from gig.models import Gig
from proFile.models import Profile
from django.contrib.auth import get_user_model
from Fiverr import settings
from django.urls import reverse
import datetime

User = get_user_model()

class Comment(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, null=True, related_name='comment_gig')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    subject = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=30,  null=True)
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
    

    def time_ago(self):
        now = datetime.datetime.now()

        delta = now - self.publish

        format_delta = delta.total_seconds()

        years = format_delta // (60 * 60 * 24 * 30 * 12)

        months = format_delta // (60 * 60 * 24 * 30)

        days = format_delta // (60 * 60 * 24) 

        hours = format_delta // (60 * 60)

        minutes = format_delta // 60

        seconds = format_delta
        if seconds > 60:
            while months > 11.99:
                months -= 12

            while days > 29.99:
                days -= 30

            while hours > 23.99:
                hours -= 24

            while minutes > 59.99:
                minutes -= 60

            while seconds > 59.99:
                seconds -= 60

            date = ''
            if years > 0:
                if years == 1:
                    date += int(years) + ' year'
                else:
                    date += int(years) + ' years'
            if months > 0:
                if months == 1:
                    date += ' , ' + str(int(months)) + ' month'
                else:
                    date += ' , ' + str(int(months)) + ' months'
            if days > 0:
                if days == 1:
                    date += ' , ' + str(int(days))  + ' day'
                else:
                    date += ' , ' + str(int(days))  + ' days'
            if hours > 0:
                if hours == 1:
                    date += ' , ' + str(int(hours)) + ' hour'
                else:
                    date += ' , ' + str(int(hours)) + ' hours'
            if minutes > 0:
                date += ' , ' + str(int(minutes)) + ' minutes'

            date += ' ago'
            if years == 0:
                date = date[3:]
            return date
        else:
            return 'moments ago'