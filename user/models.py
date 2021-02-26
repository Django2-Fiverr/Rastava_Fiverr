from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


# Create custom User table using required fields or override predefined fields
class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    email = models.EmailField(_('email address'))
    phone_number = models.CharField(
        _('Phone number'), max_length=11, blank=True, null=True)
    age = models.CharField(_('age'), max_length=3, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return f'{self.username}'
