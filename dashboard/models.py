from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string

from account.models import User, Company, Category

# Create your models here.
from price import settings


class SocialMedia(models.Model):
    name = models.CharField(max_length=30, blank=True)
    url = models.URLField()


class TypeDiscount(models.Model):
    name = models.CharField(max_length=30, blank=True)
    percent = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=30, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(max_length=30, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    discount = models.CharField(max_length=30, blank=True)
    type = models.ForeignKey(TypeDiscount, on_delete=models.CASCADE)
    total_number = models.IntegerField(blank=True)
    number = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return '%s' % self.id


class OrderProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def get_final_product_price(self):
        return self.get_total_product_price()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    def get_total(self):
        total = 0
        for order_product in self.product.all():
            total += order_product.get_final_product_price()
        return total


class Referral(models.Model):
    referral_token = models.TextField(max_length=4, blank=False, default=get_random_string(length=32), editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ReferralLink(models.Model):
    link = models.URLField()
    referral = models.CharField(max_length=30, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ReferredLink(models.Model):
    link = models.URLField()
    referral = models.CharField(max_length=30, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
