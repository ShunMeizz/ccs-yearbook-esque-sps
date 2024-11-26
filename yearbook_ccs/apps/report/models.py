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

    user_reported = models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,blank=True, related_name="user_reported")
    reason = models.CharField(max_length=200, null=True, blank=True)
    report_type = models.IntegerField(choices=REPORT_TYPE_CHOICES,null=False,default=0) #default 0 ??? 
    status = models.IntegerField(choices=PENDING_CHOICES,null=False,default=0)
    date = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    link = models.URLField(null=True, blank=True) #kani unsaon dae

class PostReport(models.Model):
    post_id = models.ForeignKey(Blog, null=False, blank=False,related_name="blog_post")
    report_id = models.ForeignKey(Report, null=False, blank=False, related_name="blog_report")
