from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [



    
    path('trainer/', views.trainer, name="trainer"),
    path('trainee/', views.trainee, name="trainee"),
	path('logout/', views.logoutUser, name="logout"),

    path('' , views.login_attempt , name="login_attempt"),
	path('home/' ,views.home  , name="home"),
    path('register/' , views.register_attempt , name="register_attempt"),
    path('login/' , views.login_attempt , name="login_attempt"),
    path('token/' , views.token_send , name="token_send"),
    path('success/' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error/' , views.error_page , name="error")


]