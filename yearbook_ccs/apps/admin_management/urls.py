from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_home'),
    path('review_acc/', views.review_user_verification_requests, name='review_acc'),
    path('view_users', views.view_user_accounts, name='view_users')
]