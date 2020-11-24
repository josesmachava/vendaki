from django.contrib import admin
from .models import User


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']



class CompanyAdmin(admin.ModelAdmin):
    list_display = ['commercial_name']



class ReferralAdmin(admin.ModelAdmin):
    list_display = ['referral_token']

class UserAdmin(admin.ModelAdmin):
    list_display = ['phone_number']

class ReferralLinkAdmin(admin.ModelAdmin):
    list_display = ['link']


admin.site.register(User, UserAdmin)

