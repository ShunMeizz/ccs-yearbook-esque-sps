from django.db import models
from ..user_management.models import UserAccount
# Create your models here.x
class UserProfile(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    program = models.CharField(max_length=50, null=True)
    batch_year = models.IntegerField(null=True)
    quote = models.TextField(max_length=250, null=True)
    hobbies = models.TextField(blank=True, null=True)
    favorite_quote = models.TextField(blank=True, null=True)
    facebook_link = models.TextField(max_length=250, null=True)
    linkedin_link = models.TextField(max_length=250, null=True) 
    github_link = models.TextField(max_length=250, null=True)
    instagram_link = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.first_name

