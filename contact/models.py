from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject =models.CharField(max_length=50)
    message =models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, null= True)

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return self.name
