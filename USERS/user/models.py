from django.db import models


# Create your models here.
class User(models.Model):
    objects = None
    name = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000, unique=True)
    date_publication = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PersonalInformation(models.Model):
    objects = None
    name = models.CharField(max_length=20)
    status = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return self.name
