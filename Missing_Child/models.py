from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Child(models.Model):

    name = models.CharField(max_length=50, blank=False)
    age = models.IntegerField( blank=False)
    details = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to = 'pic_folder/')
