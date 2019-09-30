from django.contrib import admin
from .models import Profile, Company
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Profile, ProfileAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['comercial_name']

admin.site.register(Company, CompanyAdmin)
