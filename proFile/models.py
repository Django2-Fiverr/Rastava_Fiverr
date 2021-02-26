from django.db import models
# from django.contrib.auth import get_user_model
from user.models import User
from category.models import Category


# User=get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True,blank=True)
    bio = models.TextField(max_length=1000, help_text='User bio')
    skills = models.ManyToManyField(Category, help_text='Choose Your Skills',blank=True)
    birth = models.DateField('Birth', null=True, blank=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True) 
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
