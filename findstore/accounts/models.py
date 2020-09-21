from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    uid=models.IntegerField(primary_key=True,auto_created=True)
    email=models.CharField(max_length=50, null=True)
    password=models.CharField(max_length=50, null=True)
    nickname=models.CharField(max_length=50, null=True)
    sex=models.CharField(max_length=50, null=True)
    age=models.IntegerField(null=True)
