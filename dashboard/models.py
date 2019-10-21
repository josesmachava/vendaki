from django.db import models
from account.models import  User

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


class OrderProduct():
    item = models.ForeignKey(Product, on_delete=models.CASCADE())


class Order(models.Model):
    user = models.ForeignKey(User)
    product = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name
