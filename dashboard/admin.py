from django.contrib import admin
from .models import *
# Register your models here.

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['name']



class ReferralAdmin(admin.ModelAdmin):
    list_display = ['referral_token']


class ReferralLinkAdmin(admin.ModelAdmin):
    list_display = ['link']


class ReferredLinkAdmin(admin.ModelAdmin):
    list_display = ['link']


admin.site.register(SocialMedia, SocialMediaAdmin)

admin.site.register(Product)

admin.site.register(TypeDiscount)

admin.site.register(OrderProduct)

admin.site.register(Order)
admin.site.register(Category)
admin.site.register(ReferralLink, ReferralLinkAdmin)

admin.site.register(ReferredLink, ReferredLinkAdmin)

admin.site.register(Referral, ReferralAdmin)






