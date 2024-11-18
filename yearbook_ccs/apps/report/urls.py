from django.urls import path
from . import views

urlpatterns = [
    path('reports/',views.report_home,name="report"),
    path('reports/add_report',views.add_report,name="add_report")
]