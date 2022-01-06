from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .import views 
from .views import *

urlpatterns = [



    
    path('trainer/', views.trainer, name="trainer"),
    #path('trainee/', views.trainee, name="trainee"),
	path('logout/', views.logoutUser, name="logout"),
	
    path('pagedetail/<int:id>/',views.page_detail, name='pagedetail'),
    path('faq/',views.faq_list, name='faq'),
    path('enquiry/',views.enquiry_list, name='enquiry'),

	path('' ,views.home  , name="home"),
    path('register/' , views.register_attempt , name="register_attempt"),
    path('login_attempt/' , views.login_attempt , name="login_attempt"),
    path('token/' , views.token_send , name="token_send"),
    
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error/' , views.error_page , name="error"),
    path('notifs',views.notifs,name='notifs'),
	path('get_notifs',views.get_notifs,name='get_notifs'),
	path('mark_read_notif',views.mark_read_notif,name='mark_read_notif'),
    path('video',views.video,name='video'),
    path('gallery',views.gallery,name='gallery'),
    path('gallerydetail/<int:id>',views.gallery_detail,name='gallery_detail'),
	path('pricing',views.pricing,name='pricing'),
    path('checkout/<int:plan_id>',views.checkout,name='checkout'),
    path('udashboard',views.udashboard,name='udashboard'),
    path('update_profile',views.update_profile,name='update_profile'),
    #TrainerLogin
    path('trainerlogin',views.trainerlogin,name='trainerlogin'),
    path('trainerlogout',views.trainerlogout,name='trainerlogout'),
    path('trainer_dashboard',views.trainer_dashboard,name='trainer_dashboard'),
    path('trainer_profile',views.trainer_profile,name='trainer_profile'),
    path('trainer_subscribers',views.trainer_subscribers,name='trainer_subscribers'),
    path('trainer_payments',views.trainer_payments,name='trainer_payments'),
    path('trainer_changepassword',views.trainer_changepassword,name='trainer_changepassword'),
    path('trainer_notifs',views.trainer_notifs,name='trainer_notifs'),
    path('messages',views.trainer_msgs,name='messages'),
   
    path('report_for_user',views.report_for_user,name='report_for_user'),
	path('report_for_trainer',views.report_for_trainer,name='report_for_trainer'),

    #Password Reset
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="gym/password_reset.html"),
    name="reset_password"),
    path('checkout_session/<int:plan_id>',views.checkout_session,name='checkout_session'),
	path('pay_success',views.pay_success,name='pay_success'),
	path('pay_cancel',views.pay_cancel,name='pay_cancel'),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="gym/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="gym/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="gym/password_reset_done.html"), 
        name="password_reset_complete"),
    #PASSWORD cHANGE
    path('password/', PasswordsChangeView.as_view(template_name='gym/User/change-password.html'),name='password'),
    
      
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)