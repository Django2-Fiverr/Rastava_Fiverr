import os
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q
from category.models import Category

# use the custom user table ( the default one in settings.py) 
User = get_user_model()


# This function splits file name and its format ( one.jpg -> one + .jpg )
def split_name(file_name):
    base_name = os.path.basename(file_name)
    name, format = os.path.splitext(base_name)
    return name, format


# This function changes default file name and uses the same format ( one.jpg -> two.jpg )
# it returns an address to save the uploaded image file
def get_name(instance, file_name):
    name, format = split_name(file_name)
    new_name = '{}-{}{}'.format(instance.user.username, instance.slug, format)
    return 'gigs/{}'.format(new_name)


# Gis manager class which customizes gig objects methods
class GigManager(models.Manager):
    def get_active_gigs(self):
        return self.get_queryset().filter(active=True)  # returns active ( available gigs )

    def search(self, query):  # This one requires category table ( going to be fixed later )
        pass


class Gig(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=20, blank=True, )
    cost = models.IntegerField()
    description = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sell_count = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to=get_name, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True, null=True)

    objects = GigManager()  # the previous class (Gig menager)

    # returns the name of the gig owner
    def __str__(self):
        return f'{self.user.username}-{self.category}'
