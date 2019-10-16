from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    name = models.CharField(max_length=30, blank=True)
    url = models.URLField()

class Categories(models.Model):
    name = models.CharField(max_length=30, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=30, blank=True)
    price = models.CharField(max_length=30, blank=True)
    description = models.TextField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)
    discount = models.CharField(max_length=30, blank=True)


