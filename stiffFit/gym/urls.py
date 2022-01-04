from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .import views

urlpatterns = [



    
    path('trainer/', views.trainer, name="trainer"),
    path('trainee/', views.trainee, name="trainee"),
	path('logout/', views.logoutUser, name="logout"),
	
    path('pagedetail/<int:id>/',views.page_detail, name='pagedetail'),
    path('faq/',views.faq_list, name='faq'),
    path('enquiry/',views.enquiry_list, name='enquiry'),

	path('home/' ,views.home  , name="home"),
    path('register/' , views.register_attempt , name="register_attempt"),
    path('' , views.login_attempt , name="login_attempt"),
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
    
    path('udashboard',views.udashboard,name='udashboard'),
    path('update_profile',views.update_profile,name='update_profile'),
    #TrainerLogin
    path('trainerlogin',views.trainerlogin,name='trainerlogin'),
    path('trainerlogout',views.trainerlogout,name='trainerlogout'),
    path('trainer_dashboard',views.trainer_dashboard,name='trainer_dashboard'),
    path('trainer_profile',views.trainer_profile,name='trainer_profile'),
    path('trainer_changepassword',views.trainer_changepassword,name='trainer_changepassword'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)