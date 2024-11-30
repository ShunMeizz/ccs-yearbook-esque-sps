from django.contrib import admin
from .models import Report

# Register your models here.
@admin.register(Report)
class Blog(admin.ModelAdmin):
    list_display = ['user_reported','reason','report_type','status','date','link']