from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'), 
    path('account/', views.account_view, name='account'),
    path('signup-step1/', views.signup_step1, name='signup_step1'),
    path('signup-step2/', views.signup_step2, name='signup_step2'),
]