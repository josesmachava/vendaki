from django.contrib import admin
from .models import Company, User, Type, Referral


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']



class CompanyAdmin(admin.ModelAdmin):
    list_display = ['commercial_name']



class ReferralAdmin(admin.ModelAdmin):
    list_display = ['referral_token']

class UserAdmin(admin.ModelAdmin):
    list_display = ['phone_number']


admin.site.register(Type)

admin.site.register(Company, CompanyAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Referral, ReferralAdmin)

