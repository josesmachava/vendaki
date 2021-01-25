from django.db import models

# Create your models here.
from account.models import User, Store
from django.core.validators import RegexValidator
from dashboard.models import OrderProduct


class Payment(models.Model):
    order = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    status_code = models.CharField(max_length=255, null=False)
    phone_regex = RegexValidator(regex=r'^\+?84?\d{8,8}$',
                                 message="O número de telefone deve ser digitado no formato: '841234567'. São permitidos até 9 dígitos.")
    número_de_telefone = models.CharField(validators=[phone_regex], max_length=9, blank=True,
                                          unique=False)  # validators should be a list

    created_date = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.número_de_telefone}'
