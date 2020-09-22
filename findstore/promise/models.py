from django.db import models
from django.conf import settings
from meeting.models import Meeting

# Create your models here.
class Promise(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    gu =  models.CharField(max_length=200)
    dong =  models.CharField(max_length=200)
    storelist = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="meeting")