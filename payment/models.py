from django.db import models

# Create your models here.
from account.models import User
from django.core.validators import RegexValidator


from dashboard.models import Order


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)

    phone_regex = RegexValidator(regex=r'^\+?84?\d{8,8}$',
                                 message="O número de telefone deve ser digitado no formato: '849394995'. São permitidos até 13 dígitos.")
    número_de_telefone = models.CharField(validators=[phone_regex], max_length=13, blank=True,
                                          unique=False)  # validators should be a list

    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order.user.first_name}, {self.order.donation.price}'
