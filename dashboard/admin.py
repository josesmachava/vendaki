from django.contrib import admin
from .models import *
# Register your models here.

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(SocialMedia, SocialMediaAdmin)

admin.site.register(Product)

admin.site.register(TypeDiscount)

admin.site.register(OrderProduct)

admin.site.register(Order)
admin.site.register(Category)






