from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profiles_home, name='profile_home'),
]