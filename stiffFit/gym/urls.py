from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .import views

urlpatterns = [



    
    path('trainer/', views.trainer, name="trainer"),
    path('trainee/', views.trainee, name="trainee"),
	path('logout/', views.logoutUser, name="logout"),
	path('logout/', views.logoutUser, name="logout"),
    path('pagedetail/<int:id>/',views.page_detail, name='pagedetail'),
    path('faq/',views.faq_list, name='faq'),
    path('enquiry/',views.enquiry_list, name='enquiry'),

	path('home/' ,views.home  , name="home"),
    path('register/' , views.register_attempt , name="register_attempt"),
    path('' , views.login_attempt , name="login_attempt"),
    path('token/' , views.token_send , name="token_send"),
    
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error/' , views.error_page , name="error")


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)