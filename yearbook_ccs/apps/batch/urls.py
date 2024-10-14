from django.urls import path
from . import views

urlpatterns = [
    path('batch_page/', views.batch_page_view, name='batch_page'),
]