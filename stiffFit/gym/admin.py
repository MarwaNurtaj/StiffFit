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

