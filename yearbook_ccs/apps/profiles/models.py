from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    #to do how to call the User Account, have it as a foreign key to this model?
    favorite_quote = models.TextField(blank=True)
    hobbies = models.TextField(blank=True)
    #social_links = models.JSONField(default=dict, blank=True)  

    def __str__(self):
        return self.user.username
