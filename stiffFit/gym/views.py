from gym.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
# Create your views here.


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('login_attempt')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('login_attempt')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login_attempt')
        
        login(request , user)
        return redirect('home')

    return render(request , 'gym/login.html')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('register_attempt')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('register_attempt')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('token_send')

        except Exception as e:
            print(e)


    return render(request , 'gym/register.html')

def success(request):
    return render(request , 'gym/success.html')


def token_send(request):
    return render(request , 'gym/token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login_attempt')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login_attempt')
        else:
            return redirect('error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'gym/error.html')


# Create your views here.
from .models import*
@login_required
def home(request):    
    return render(request,'gym/homepage.html')

def trainer(request):
	return render(request,'gym/trainer.html')

def trainee(request):
    trainee = Trainee.objects.all()
    package = Package.objects.all()
    progress = Progress.objects.all()
    
    total_trainee = trainee.count()
    pending = progress.filter(status='Pending').count()
    progressing = progress.filter(status='Progressing').count()
    completed = progress.filter(status='Completed').count()
    
    context = {'trainee': trainee, 'package':package, 'progress':progress, 'total_trainee':total_trainee, 'pending':pending, 'progressing':progressing, 'completed':completed}
    return render(request,'gym/trainee.html', context)

def page_detail(request,id):
    page=Page.objects.get(id=id)
    return render(request, 'gym/page.html' , {'page':page})


def logoutUser(request):
	logout(request)
	return redirect('login_attempt')








def send_mail_after_registration( email , token):
    subject = 'Your accounts need to be verified (StiffFit) '
    message = f'Welcome to StiffFit.Just copy and paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    



def faq_list(request):
    faq=Faq.objects.all()
    return render(request, 'gym/faq.html' ,{'faqs':faq})

def enquiry_list(request):
	msg=''
	if request.method=='POST':
		form=forms.EnquiryForm(request.POST)
		if form.is_valid():
			form.save()
			msg='Data has been saved'
	form=forms.EnquiryForm
	return render(request, 'gym/enquiry.html',{'form':form,'msg':msg})