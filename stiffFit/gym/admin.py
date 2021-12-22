from django.contrib import admin
from . import models
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_test','image_tag')
admin.site.register(models.Banners)

admin.site.register(models.Profile)

class PageAdmin(admin.ModelAdmin):
    list_display=('alt_test',)
admin.site.register(models.Page)

class FaqAdmin(admin.ModelAdmin):
    list_display=('quest',)
admin.site.register(models.Faq,FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('full_name','email','detail',)
admin.site.register(models.Enquiry,EnquiryAdmin)