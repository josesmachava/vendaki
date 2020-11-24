# Create your models here.
from account.models import User, Store
from price import settings
from tinymce import models as tinymce_models
from s3direct.fields import S3DirectField
from django.db import models


class SocialMedia(models.Model):
    name = models.CharField(max_length=30, blank=True)
    url = models.URLField()


class Product(models.Model):
    name = models.CharField(max_length=30, blank=True)
    image = S3DirectField(dest='images')
    price = models.CharField(max_length=30, blank=True)
    description = tinymce_models.HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    visible = models.BooleanField(default=False)
    file = S3DirectField(dest='pdf')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return '%s' % self.id

    def get_discount_price_per_click(self):
        return self.price / self.total_number_of_click


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


