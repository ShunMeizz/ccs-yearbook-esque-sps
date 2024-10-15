from django.db import models
from ..user_management.models import UserAccount
from datetime import datetime
# Create your models here.x
class UserProfile(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    profile_pic = models.ImageField(upload_to='media/profile_pictures', null=True, blank=True)
    program = models.CharField(
                max_length=4,
                choices = [("BSCS", "BSCS"), ("BSIT", "BSIT")],
                default="None"
               )
    batch_year = models.IntegerField(
        choices=[(i, i) for i in range((datetime.now()).year + 4, 1986, -1)],
                    default=datetime.now().year
                )
    quote = models.TextField(max_length=250, null=True, blank =True)
    hobbies = models.TextField(blank=True, null=True)
    facebook_link = models.TextField(max_length=250, null=True,blank=True)
    facebook_link_hidden = models.BooleanField(null=True, default=True)
    linkedin_link = models.TextField(max_length=250, null=True, blank=True) 
    linkedin_link_hidden = models.BooleanField(null=True, default=True)
    github_link = models.TextField(max_length=250, null=True, blank=True)
    github_link_hidden = models.BooleanField(null=True, default=True)
    instagram_link = models.TextField(max_length=250, null=True, blank=True)
    instagram_link_hidden = models.BooleanField(null=True, default=True)
    is_hide = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.first_name
