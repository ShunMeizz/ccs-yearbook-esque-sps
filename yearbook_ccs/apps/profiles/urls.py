from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profiles_home, name='profile_home'),
    path('setup_profile/', views.setup_profile_2_view, name='setup_profile_2'),
    path('setup_profile/<uidb64>/<token>', views.setup_profile_view, name='setup_profile'),
    path('batch_page/', views.batch_page_view, name='batch_page'),
]