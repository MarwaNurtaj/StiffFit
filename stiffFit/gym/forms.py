
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from django import forms
from .models import *
from . import models
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class EnquiryForm(forms.ModelForm):
	class Meta:
		model=Enquiry
		fields=('full_name','email','detail')

class ProfileForm(UserChangeForm):
	class Meta:
		model=User
		fields=('first_name','last_name','email','username')

class TrainerLoginForm(forms.ModelForm):
	pwd = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=models.Trainer
		fields=('username','pwd')
  
class TrainerProfileForm(forms.ModelForm):
    	class Meta:
         model=models.Trainer
         fields=('trainer','phone','email','img')
         
class TrainerChangePassword(forms.Form):
    new_password=forms.CharField(max_length=50,required=True)
