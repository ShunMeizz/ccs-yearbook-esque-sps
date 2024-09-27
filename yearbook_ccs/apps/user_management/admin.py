from django.contrib import admin
from .models import UserAccount
from imagekit.admin import AdminThumbnail

@admin.register(UserAccount)
class UserAccount(admin.ModelAdmin):
    list_display = ['user', 'id_front_display', 'id_back_display', 'is_acc_verified']

    id_front_display = AdminThumbnail(image_field='id_front')
    id_back_display = AdminThumbnail(image_field='id_back')

    id_front_display.short_description = 'ID Front'
    id_back_display.short_description = 'ID Back'
