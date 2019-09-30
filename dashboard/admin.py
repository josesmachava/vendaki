from django.contrib import admin
from .models import SocialMedia
# Register your models here.

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(SocialMedia, SocialMediaAdmin)



