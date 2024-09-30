from django.contrib import admin
from .models import UserAccount
from imagekit.admin import AdminThumbnail

admin.site.register(UserAccount)