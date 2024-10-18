from django.contrib import admin
from .models import Comment, ProfileComment, BlogComment
# Register your models here.
admin.site.register(ProfileComment)
admin.site.register(BlogComment)