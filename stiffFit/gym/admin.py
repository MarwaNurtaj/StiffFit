from django.contrib import admin
from . import models
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_test','image_tag')
admin.site.register(models.Banners)

admin.site.register(models.Profile) 
admin.site.register(models.Trainer) 
admin.site.register(models.Trainee)
admin.site.register(models.Package) 
admin.site.register(models.Progress) 



class PageAdmin(admin.ModelAdmin):
    list_display=('alt_test',)
admin.site.register(models.Page)

class FaqAdmin(admin.ModelAdmin):
    list_display=('quest',)
admin.site.register(models.Faq,FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('full_name','email','detail',)
admin.site.register(models.Enquiry,EnquiryAdmin)