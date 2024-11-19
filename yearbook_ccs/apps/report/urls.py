from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/reports/',views.report_home,name="report"),
    path('reports/add_report',views.add_report,name="add_report"),
    path('reports/finished',views.finished_report,name="finished_report")
]