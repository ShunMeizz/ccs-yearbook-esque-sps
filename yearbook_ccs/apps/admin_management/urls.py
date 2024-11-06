from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_home'),
    path('review_acc/', views.review_user_account, name='review_acc'),
]