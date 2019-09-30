from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    name = models.CharField(max_length=30, blank=True)
    url = models.URLField()
   