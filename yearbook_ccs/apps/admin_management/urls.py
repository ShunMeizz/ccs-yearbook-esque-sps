from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/review_acc/', views.review_user_account, name='review_acc'),
]