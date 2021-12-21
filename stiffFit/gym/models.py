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
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(default="default_profile.jpg",null=True, blank=True)
	
    def __str__(self):
        return self.name
    
class Trainee(models.Model):
    name = models.CharField(max_length=200, null=True)
    age = models.FloatField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(default="default_profile.jpg",null=True, blank=True)
	
    def __str__(self):
        return self.name

 
    
    
