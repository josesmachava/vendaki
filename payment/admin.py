from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from payment.models import *




class PaymentAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Payment, PaymentAdmin)
