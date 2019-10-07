from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    name = models.CharField(max_length=30, blank=True)
    url = models.URLField()

class Categories(models.Model):
    name = models.CharField(max_length=30, blank=True)


class Products(models.Model):
    name = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=30, blank=True)
    price = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)
    descont = models.CharField(max_length=30, blank=True)


