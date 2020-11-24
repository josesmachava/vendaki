from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from payment.models import *


class DonationAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Donation, DonationAdmin)




class DonationAdmin(admin.ModelAdmin):
    list_display = ['name']



class PaymentAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Payment, PaymentAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Order, OrderAdmin)
