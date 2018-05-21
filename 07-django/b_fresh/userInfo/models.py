from django.db import models


# Create your models here.

class userInfo(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
