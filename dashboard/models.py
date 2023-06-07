# Create your models here.
from account.models import User, Store
from price import settings
from s3direct.fields import S3DirectField
from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from tinymce import models as tinymce_models


class SocialMedia(models.Model):
    name = models.CharField(max_length=30, blank=True)
    url = models.URLField()


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=True)
    price = models.CharField(max_length=30, blank=True)
    image = S3DirectField(dest='images')
    description = tinymce_models.HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=False)
    file = S3DirectField(dest='pdf')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


class OrderProduct(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    name = models.CharField(max_length=255, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    phone_regex = RegexValidator(regex=r'^\+?84?\d{8,8}$',
                                 message="O número de telefone deve ser digitado no formato: '841234567'. São permitidos até 9 dígitos.")
    número_de_telefone = models.CharField(validators=[phone_regex], max_length=9, blank=True,
                                          unique=False)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_product_price(self):
        return self.quantity * self.product.price

    def get_final_product_price(self):
        return self.get_total_product_price()


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    product = models.ManyToManyField(OrderProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    phone_regex = RegexValidator(regex=r'^\+?84?\d{8,8}$',
                                 message="O número de telefone deve ser digitado no formato: '841234567'. São permitidos até 9 dígitos.")
    número_de_telefone = models.CharField(validators=[phone_regex], max_length=9, blank=True,
                                          unique=False)

    def __str__(self):
        return self.store.name

    def get_total(self):
        total = 0
        for order_product in self.product.all():
            total += order_product.get_final_product_price()
        return total
