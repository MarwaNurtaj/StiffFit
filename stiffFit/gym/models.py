from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Banners(models.Model):
    img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)

    def __str__(self):
        return self.alt_text

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.img.url))
    
class Trainer(models.Model):
    CATEGORY = (
                ('Yoga Trainer', 'Yoga Trainer'),
                ('Gym Master', 'Gym Master'),
                ('Nutritionist', 'Nutritionist'),
                )
    trainer = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(default="default_profile.jpg",null=True, blank=True)
	
    def __str__(self):
        return self.trainer
    
class Trainee(models.Model):
    trainee = models.CharField(max_length=200, null=True)
    age = models.FloatField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(default="default_profile.jpg",null=True, blank=True)
	
    def __str__(self):
        return self.trainee
    
class Package(models.Model):
    TYPE = (
                ('Yoga', 'Yoga'),
                ('Gym', 'Gym'),
                ('Balanced Nutrition Diet', 'Balanced Nutrition Diet'),
                )
    package = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=TYPE)
    date_of_enrolment = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.package

class Progress(models.Model):
    STATUS = (
                ('Not Applicable', 'Not Applicable' ),
		        ('Pending', 'Pending'),
                ('Progressing', 'Progressing' ),
                ('Completed', 'Completed'),
             )
    trainee = models.ForeignKey(Trainee, null=True, on_delete=models.SET_NULL)
    trainer = models.ForeignKey(Trainer, null=True, on_delete=models.SET_NULL)
    package = models.ForeignKey(Package, null=True, on_delete=models.SET_NULL)
    date_of_enrolment = models.DateTimeField(auto_now_add=True, null = True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    
    

 
    
    
