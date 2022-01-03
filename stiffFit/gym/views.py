from .models import*
from gym.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from django.core import serializers
from django.http import JsonResponse
# Create your views here.


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('login_attempt')

        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.is_verified:
            messages.success(
                request, 'Profile is not verified check your mail.')
            return redirect('login_attempt')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login_attempt')

        login(request, user)
        return redirect('home')

    return render(request, 'gym/login.html')


def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username is taken.')
                return redirect('register_attempt')

            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('register_attempt')

            user_obj = User(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(
                user=user_obj, auth_token=auth_token)
            profile_obj.save()
            send_mail_after_registration(email, auth_token)
            return redirect('token_send')

        except Exception as e:
            print(e)

    return render(request, 'gym/register.html')


def success(request):
    return render(request, 'gym/success.html')


def token_send(request):
    return render(request, 'gym/token_send.html')


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()

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
    return render(request, 'gym/error.html')


# Create your views here.



def home(request):
    return render(request, 'gym/homepage.html')


def trainer(request):
    return render(request, 'gym/trainer.html')


def trainee(request):
    trainee = Trainee.objects.all()
    package = Package.objects.all()
    progress = Progress.objects.all()

    total_trainee = trainee.count()
    pending = progress.filter(status='Pending').count()
    progressing = progress.filter(status='Progressing').count()
    completed = progress.filter(status='Completed').count()

    context = {'trainee': trainee, 'package': package, 'progress': progress, 'total_trainee': total_trainee,
               'pending': pending, 'progressing': progressing, 'completed': completed}
    return render(request, 'gym/trainee.html', context)


def page_detail(request, id):
    page = Page.objects.get(id=id)
    return render(request, 'gym/page.html', {'page': page})


def logoutUser(request):
    logout(request)
    return redirect('login_attempt')


def notifs(request):
    data = Notify.objects.all().order_by('-id')
    return render(request, 'gym/notification.html')

# Get All Notifications


def get_notifs(request):
    data = models.Notify.objects.all().order_by('-id')
    notifStatus = False
    jsonData = []
    totalUnread = 0
    for d in data:
        try:
            notifStatusData = models.NotifUserStatus.objects.get(
                user=request.user, notif=d)
            if notifStatusData:
                notifStatus = True
        except models.NotifUserStatus.DoesNotExist:
            notifStatus = False
        if not notifStatus:
            totalUnread = totalUnread+1
        jsonData.append({
                        'pk': d.id,
                        'notify_detail': d.notify_detail,
                        'notifStatus': notifStatus
                        })
    # jsonData=serializers.serialize('json', data)
    return JsonResponse({'data': jsonData, 'totalUnread': totalUnread})

# Mark Read By user


def mark_read_notif(request):
    notif = request.GET['notif']
    notif = models.Notify.objects.get(pk=notif)
    user = request.user
    models.NotifUserStatus.objects.create(notif=notif, user=user, status=True)
    return JsonResponse({'bool': True})


def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified (StiffFit) '
    message = f'Welcome to StiffFit.Just copy and paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def faq_list(request):
    faq = Faq.objects.all()
    return render(request, 'gym/faq.html', {'faqs': faq})


def enquiry_list(request):
    msg = ''
    if request.method == 'POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'Data has been saved'
    form = forms.EnquiryForm
    return render(request, 'gym/enquiry.html', {'form': form, 'msg': msg})


def video(request):
    return render(request, 'gym/video.html')


def gallery(request):
    gallery = Gallery.objects.all().order_by('-id')
    return render(request, 'gym/gallery.html', {'galleries': gallery})


def gallery_detail(request, id):
    gallery = Gallery.objects.get(id=id)
    gallery_imgs = GalleryImage.objects.all().filter(gallery=gallery).order_by('-id')
    return render(request, 'gym/gallery_imgs.html', {'gallery_imgs': gallery_imgs, 'gallery': gallery})

# Subscription Plans


def pricing(request):
    pricing = SubPlan.objects.all()
    #annotate(total_members=Count('subscription__id')).all().order_by('price')
    dfeatures = SubPlanFeature.objects.all()
    return render(request, 'gym/pricing.html', {'plans': pricing, 'dfeatures': dfeatures})


def udashboard(request):

    return render(request, 'gym/dashboard.html')


def update_profile(request):
    msg = None
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg = 'Data has been Updated'
    form = forms.ProfileForm(instance=request.user)
    return render(request, 'gym/update_profile.html', {'form': form, 'msg': msg})


# trainer login
def trainerlogin(request):
	msg=''
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['pwd']
		trainer=Trainer.objects.filter(username=username,pwd=password).count()
		if trainer > 0:
			trainer=Trainer.objects.filter(username=username,pwd=password).first()
			request.session['trainerLogin']=True
			request.session['trainerid']=trainer.id
			return redirect('/trainer_dashboard')
		else:
			msg='Invalid!!'
	form=forms.TrainerLoginForm
    
	return render(request, 'gym/Trainer/Trainerlogin.html',{'form':form,'msg':msg})

# Trainer Logout
def trainerlogout(request):
	del request.session['trainerLogin']
	return redirect('/trainerlogin')      

# Checkout
def checkout(request, plan_id):
    planDetail = SubPlan.objects.get(pk=plan_id)
    return render(request, 'gym/checkout.html', {'plan': planDetail})
