from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'), 
    path('account/', views.account_view, name='account'),
    path('signup-step1/', views.signup_step1, name='signup_step1'),
    path('signup-step2/', views.signup_step2, name='signup_step2'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/done/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]