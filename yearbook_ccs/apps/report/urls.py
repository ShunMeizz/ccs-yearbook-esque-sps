from django.urls import path
from . import views

urlpatterns = [
    # path('reports/',views.report_home,name="report"),
    path('reports/add_report',views.add_report,name="add_report"),
    path('reports/finished',views.finished_report,name="finished_report"),
    path('reports/posts',views.report_posts,name="reports_posts"),
    path('reports/profiles',views.report_profiles,name="reports_posts"),
    path('reports/comments',views.report_comments,name="reports_posts"),
]