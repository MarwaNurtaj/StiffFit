from .utils import *
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import EmailMessage
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
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse_lazy
import stripe
from django.template.loader import get_template
from django.db.models import Count
from datetime import timedelta


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
    
    banners = Banners.objects.all()
    gimgs = GalleryImage.objects.all().order_by('-id')[:9]
    trainers=Trainer.objects.all()
    subPlans=SubPlan.objects.all()
    
    total_trainers=trainers.count()
    total_subPlans=subPlans.count()
    
    return render(request, 'gym/homepage.html', {'banners': banners, 'gimgs': gimgs, 'total_trainers': total_trainers, 'total_subPlans':total_subPlans})


def trainer(request):
    get_unread_Msg = getMsg(request) 
    return render(request, 'gym/trainer.html',{'totalUnread':get_unread_Msg})


def page_detail(request, id):
    page = Page.objects.get(id=id)
    return render(request, 'gym/page.html', {'page': page,})


def logoutUser(request):
    logout(request)
    return redirect('login_attempt')


def notifs(request):
    get_unread_Msg = getMsg(request) 
    data = Notify.objects.all().order_by('-id')
    return render(request, 'gym/notification.html',{'totalUnread':get_unread_Msg})

# Get All Notifications


def get_notifs(request):

    data = Notify.objects.all().order_by('-id')
    notifStatus = False
    jsonData = []
    totalUnread = 0
    for d in data:
        try:
            notifStatusData = NotifUserStatus.objects.get(
                user=request.user, notif=d)
            if notifStatusData:
                notifStatus = True
        except NotifUserStatus.DoesNotExist:
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
    notif = Notify.objects.get(pk=notif)
    user = request.user
    NotifUserStatus.objects.create(notif=notif, user=user, status=True)
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
    get_unread_Msg = getMsg(request) 
    gallery = Gallery.objects.all().order_by('-id')
    return render(request, 'gym/gallery.html', {'galleries': gallery,'totalUnread':get_unread_Msg})


def gallery_detail(request, id):
    get_unread_Msg = getMsg(request) 
    gallery = Gallery.objects.get(id=id)
    gallery_imgs = GalleryImage.objects.all().filter(gallery=gallery).order_by('-id')
    return render(request, 'gym/gallery_imgs.html', {'gallery_imgs': gallery_imgs, 'gallery': gallery,'totalUnread':get_unread_Msg})

# Subscription Plans


def pricing(request):
     
    pricing = SubPlan.objects.annotate(total_members=Count(
        'subscription__id')).all().order_by('price')
    dfeatures = SubPlanFeature.objects.all()
    return render(request, 'gym/pricing.html', {'plans': pricing, 'dfeatures': dfeatures})



def udashboard(request):
    get_unread_Msg = getMsg(request) 
    current_plan=Subscription.objects.get(user=request.user)
    my_trainer=AssignSubscriber.objects.get(user=request.user)
    
    enddate=current_plan.reg_date+timedelta(days=current_plan.plan.validity_days)

	
    return render(request, 'gym/User/dashboard.html',{
		'current_plan':current_plan,
		'my_trainer':my_trainer,
		'totalUnread':get_unread_Msg,
		'enddate':enddate
	})

def update_profile(request):
    msg = None
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            msg = 'Data has been Updated'
    form = forms.ProfileForm(instance=request.user)
    return render(request, 'gym/User/update_profile.html', {'form': form, 'msg': msg})


# trainer login
def trainerlogin(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pwd']
        trainer = Trainer.objects.filter(
            username=username, pwd=password).count()
        if trainer > 0:
            trainer = Trainer.objects.filter(
                username=username, pwd=password).first()
            request.session['trainerLogin'] = True
            request.session['trainerid'] = trainer.id
            return redirect('/trainer_dashboard')
        else:
            msg = 'Invalid!!'
    form = forms.TrainerLoginForm

    return render(request, 'gym/Trainer/Trainerlogin.html', {'form': form, 'msg': msg})

# Trainer Logout


def trainerlogout(request):
    del request.session['trainerLogin']
    return redirect('/trainerlogin')


# Checkout
def checkout(request, plan_id):
    planDetail = SubPlan.objects.get(pk=plan_id)
    return render(request, 'gym/checkout.html', {'plan': planDetail})


# Trainer Dashboard
def trainer_notif(request):
    return render(request, 'gym/Trainer/TrainerNotif.html')


def trainer_dashboard(request):
    return render(request, 'gym/Trainer/dashboard.html')

# Trainer Profile


def trainer_profile(request):
    msg = None
    t_id = request.session['trainerid']
    trainer = Trainer.objects.get(pk=t_id)
    if request.method == 'POST':
        form = forms.TrainerProfileForm(
            request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            msg = 'Profile has been updated'
    form = forms.TrainerProfileForm(instance=trainer)
    return render(request, 'gym/Trainer/profile.html', {'form': form})

# PAssWord Change View

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('udashboard')


# Trainer Change Password
def trainer_changepassword(request):
    # trainer=Trainer.objects.get(pk=request.session['trainerid'])
    msg = None
    if request.method == 'POST':
        new_password = request.POST['new_password']
        updateRes = Trainer.objects.filter(
            pk=request.session['trainerid']).update(pwd=new_password)
        if updateRes:
            del request.session['trainerLogin']
            return redirect('/trainerlogin')
        else:
            msg = 'Something is weong!!'

    form = forms.TrainerChangePassword
    return render(request, 'gym/Trainer/changepassword.html', {'form': form})


stripe.api_key = 'sk_test_51KDwzeG64u1vLXZgyQbB7OoppkffeNsDXjHlN2imxy9IAVObrQ1nD6oet2QTkSZdJzGLK7bxqmM1ePwvnK8viLHS00bwORfvwW'


def checkout_session(request, plan_id):
    plan = SubPlan.objects.get(pk=plan_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': plan.title,
                    },
                    'unit_amount': plan.price*100,
                    },
            'quantity': 1,
        }],
        mode='payment',

        success_url='http://127.0.0.1:8000/pay_success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://127.0.0.1:8000/pay_cancel',
        client_reference_id=plan_id

    )
    return redirect(session.url, code=303)


# Success


def pay_success(request):
    session = stripe.checkout.Session.retrieve(request.GET['session_id'])
    plan_id = session.client_reference_id
    plan = SubPlan.objects.get(pk=plan_id)
    user = request.user
    Subscription.objects.create(
        plan=plan,
        user=user,
        price=plan.price
    )
    subject = 'Order Email'
    html_content = get_template(
        'gym/orderemail.html').render({'title': plan.title})
    from_email = 'eilearn321@gmail.com'

    msg = EmailMessage(subject, html_content, from_email, [
        'stifffit2020@gmail.com'])
    msg.content_subtype = "html"  # Main content is now in text/html
    msg.send()
    return render(request, 'gym/success.html')


# Cancel

def pay_cancel(request):
    return render(request, 'gym/cancel.html')
#Trainer Notification
def trainer_notifs(request):
    data=TrainerNotification.objects.all().order_by('-id')
    return render(request, 'gym/Trainer/notif.html',{'notifs':data})


#Trainer Subscribers
def trainer_subscribers(request):
    trainer=Trainer.objects.get(pk=request.session['trainerid'])
    trainer_subs=AssignSubscriber.objects.filter(trainer=trainer).order_by('-id')
    return render(request, 'gym/Trainer/subscribers.html', {'trainer_subs':trainer_subs})


#Trainers Payments
def trainer_payments(request):
    trainer=Trainer.objects.get(pk=request.session['trainerid'])
    trainer_pays=TrainerSalary.objects.filter(trainer=trainer).order_by('-id')
    return render(request, 'gym/Trainer/payments.html', {'trainer_pays':trainer_pays})

#Trainer Messages
def trainer_msgs(request):
    data=TrainerMsg.objects.all().order_by('-id')
    return render(request, 'gym/Trainer/msgs.html',{'msgs':data})


# Report for user
def report_for_user(request):
	trainer=Trainer.objects.get(id=request.session['trainerid'])
	msg=''
	if request.method=='POST':
		form=forms.ReportForUserForm(request.POST)
		if form.is_valid():
			new_form=form.save(commit=False)
			new_form.report_from_trainer=trainer
			new_form.save()
			msg='Data has been saved'
		else:
			msg='Invalid Response!!'
	form=forms.ReportForUserForm
	return render(request, 'gym/report_for_user.html',{'form':form,'msg':msg})

# Report for trainer
def report_for_trainer(request):
	user=request.user
	msg=''
	if request.method=='POST':
		form=forms.ReportForTrainerForm(request.POST)
		if form.is_valid():
			new_form=form.save(commit=False)
			new_form.report_from_user=user
			new_form.save()
			msg='Data has been saved'
		else:
			msg='Invalid Response!!'
	form=forms.ReportForTrainerForm
	return render(request, 'gym/report_for_trainer.html',{'form':form,'msg':msg})
    
