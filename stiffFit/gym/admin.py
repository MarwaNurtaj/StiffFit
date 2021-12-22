from django.contrib import admin
from . import models
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_test')
admin.site.register(models.Banners)

admin.site.register(models.Profile) 
admin.site.register(models.Trainer) 
admin.site.register(models.Trainee)
admin.site.register(models.Package) 
admin.site.register(models.Progress) 




