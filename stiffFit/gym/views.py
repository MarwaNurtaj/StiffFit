from django.shortcuts import render
from django.shortcuts import render,redirect

from django.http import HttpResponse 
from django.forms import inlineformset_factory 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,login,logout


from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from django.core.checks import messages
from django.shortcuts import render, redirect

from django.http import HttpResponse,JsonResponse

from .forms import CreateUserForm

# Create your views here.
from .models import*
def home(request):
	return render(request,'gym/homepage.html')

def trainer(request):
	return render(request,'gym/trainer.html')

def trainee(request):
	return HttpResponse('trainee')

# Create your views here.
def registerPage(request):
		form = CreateUserForm()	
		if request.method =='POST':

			form=CreateUserForm(request.POST)
			if form.is_valid():
				user= form.save()
		context = {'form': form}
		return render(request,'gym/register.html', context)



def loginPage(request):
	if request.method =='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username OR password is incorrect')
	context = {}
	return render(request,'gym/login.html', context)
