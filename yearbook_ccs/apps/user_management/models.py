from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_front = models.ImageField(upload_to='media/id_images/front', null=True, blank=True)
    id_back = models.ImageField(upload_to='media/id_images/back', null=True, blank=True)
    is_acc_verified = models.BooleanField(default=False)
    favorite_quote = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)
    #social_links = models.JSONField(default=dict, blank=True)  

    def __str__(self):
        return self.user.username
