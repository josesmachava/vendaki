from django.contrib import admin
from .models import User, Store


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['phone_number']


admin.site.register(User, UserAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Store, StoreAdmin)
