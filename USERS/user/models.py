from django.db import models


# Create your models here.
class User(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date_publication = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
