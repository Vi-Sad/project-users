from django.db import models


# Create your models here.
class User(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)


class Post(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
