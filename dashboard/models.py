from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


from account.models import User, Company, Category

# Create your models here.
from price import settings
import qrcode
from django.db import models




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
    type_of_discount = models.ForeignKey(TypeDiscount, on_delete=models.CASCADE)
    total_number_of_click = models.IntegerField(blank=True)
    discount_price_per_click = models.IntegerField(blank=True, null=True)

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

    qrcode_image = models.ImageField(upload_to = 'qrcode')
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


def end_order(request):
    render(request)


class Referral(models.Model):
    referral_token = models.TextField(max_length=1000, blank=False, default=get_random_string(length=20),
                                      editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ReferredLink(models.Model):
    link = models.URLField()
    referral = models.CharField(max_length=30, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.referral

    def get_referral(self):
        return self.referral


def get_referral():
    pass


class ReferralLink(models.Model):
    link = models.URLField()
    referral = models.CharField(max_length=30, blank=True)
    active = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def count_referral(self):
        count = 0

        for i in ReferredLink.objects.all():
            if i.referral == self.referral and i.product.id == self.product.id:
                if not self.product.total_number_of_click == count:
                    if self.active:
                        count = count + 1
        return count

    def get_total_number(self):
        return self.product.total_number_of_click

    def get_discount_per_click(self):
        return self.product.get_discount_price_per_click()

    def get_total_discount(self):
        return self.get_discount_per_click() * self.count_referral()
