from django.db import models
from apps.user_management.models import UserAccount
from apps.blog.admin import Blog

# Create your models here.
class Report(models.Model):
    PENDING_CHOICES = [
        (0,"Pending"),
        (1,"Finished"),
    ]

    REPORT_TYPE_CHOICES = [
        (0,"Post"),
        (1,"Comment"),
        (2,"Profile"),
    ]

    REPORT_CHOICES = [
        (0,"Nudity or sexual activity"),
        (1,"Bullying or harassment"),
        (2,"Suicide, self-injury, or eating disorder"),
        (3,"Violence, hate, or exploitation"),
        (4,"Selling or promoting restricted items"),
        (5,"Scam, fraud, or impersonation"),
    ]

    user_reported = models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,blank=True, related_name="user_reported")
    reason = models.IntegerField(choices=REPORT_CHOICES,null=False,blank=False,default=1)
    report_type = models.IntegerField(choices=REPORT_TYPE_CHOICES,null=False,default=0) #default 0 ??? 
    report_item_id = models.IntegerField(null=True, blank=True,default=0)
    report_description = models.TextField(null=True, blank=True, default="")
    status = models.IntegerField(choices=PENDING_CHOICES,null=False,default=0)
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    link = models.URLField(null=True, blank=True) #kani unsaon dae

