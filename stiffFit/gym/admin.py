from django.contrib import admin
from . import models
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display=('alt_test','image_tag')
admin.site.register(models.Banners)

admin.site.register(models.Profile) 


admin.site.register(models.Package) 
admin.site.register(models.Progress) 

class NotifyAdmin(admin.ModelAdmin):
    list_display=('notify_detail', 'read_by_user')
admin.site.register(models.Notify,NotifyAdmin)    

class NotifUserStatusAdmin(admin.ModelAdmin):
    list_display=('notif','user','status')
admin.site.register(models.NotifUserStatus,NotifUserStatusAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display=('alt_test',)
admin.site.register(models.Page)

class FaqAdmin(admin.ModelAdmin):
    list_display=('quest',)
admin.site.register(models.Faq,FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('full_name','email','detail',)
admin.site.register(models.Enquiry,EnquiryAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display=('title','image_tag',)
admin.site.register(models.Gallery,GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
    list_display=('alt_text','image_tag',)
admin.site.register(models.GalleryImage,GalleryImageAdmin)

class SubPlanAdmin(admin.ModelAdmin):
	list_editable=('highlight_status','max_member')
	list_display=('title','price','max_member','highlight_status','validity_days')
admin.site.register(models.SubPlan,SubPlanAdmin)



class SubPlanFeatureAdmin(admin.ModelAdmin):
	list_display=('title',)#'subplan',)
	def subplans(self,obj):
		return " | ".join([sub.title for sub in obj.subplan.all()])
admin.site.register(models.SubPlanFeature,SubPlanFeatureAdmin)


class TrainerAdmin(admin.ModelAdmin):
	list_editable=('is_active',)
	list_display=('trainer','phone','is_active','Image_tag',)
admin.site.register(models.Trainer,TrainerAdmin)


class PlanDiscountAdmin(admin.ModelAdmin):
	list_display=('subplan','total_months','total_discount')
admin.site.register(models.PlanDiscount,PlanDiscountAdmin)

class SubscriberAdmin(admin.ModelAdmin):
	list_display=('user','image_tag','mobile')
admin.site.register(models.Subscriber,SubscriberAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
	list_display=('user','plan','price')
admin.site.register(models.Subscription,SubscriptionAdmin)


class TrainerSalaryAdmin(admin.ModelAdmin):
	list_display=('trainer','amt','amt_date')
admin.site.register(models.TrainerSalary,TrainerSalaryAdmin)
