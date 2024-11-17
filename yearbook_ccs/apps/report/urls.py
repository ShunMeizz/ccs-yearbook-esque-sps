from django.urls import path
from . import views

urlpatterns = [
    path('report/',views.report_home,name="report")
]