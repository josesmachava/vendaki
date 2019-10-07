from django.contrib import admin
from .models import Company
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']



class CompanyAdmin(admin.ModelAdmin):
    list_display = ['commercial_name']

admin.site.register(Company, CompanyAdmin)
