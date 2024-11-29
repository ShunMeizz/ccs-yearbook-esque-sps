from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_home'),
    path('review_acc/', views.review_user_verification_requests, name='review_acc'),
    path('view_users', views.view_user_accounts, name='view_users'),
    path('profile/<int:profile_id>', views.edit_profile, name='edit_profile'),
    path('profile/default/<int:profile_id>', views.set_default_profile, name='edit_profile'),
    path('blogs', views.manage_blogs, name='manage_blogs')
]