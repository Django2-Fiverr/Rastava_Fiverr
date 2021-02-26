from django.db import models
# from django.contrib.auth import get_user_model
from user.models import User


# User=get_user_model()

class Skills(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    bio = models.TextField(max_length=1000, help_text='User bio')
    birth = models.DateField('Birth', null=True, blank=True)
    skills = models.ManyToManyField(Skills, help_text='Choose Your Skills',blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True) 
    last_update = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

