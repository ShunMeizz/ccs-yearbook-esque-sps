from django.contrib import admin
from .models import Blog

# Register your models here.
# admin.site.register(Blog)
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ['post_msg','isApproved']