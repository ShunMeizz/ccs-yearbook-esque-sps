from django.urls import path
from . import views

urlpatterns = [
    path('batch_page/', views.batch_page, name='batch_page'),
    path('search_profile/', views.search_profile, name='search_profile'),
]