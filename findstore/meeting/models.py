from django.db import models
from django.conf import settings


# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    background_img = models.TextField()
    avg_age = models.IntegerField()
    ppl = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    