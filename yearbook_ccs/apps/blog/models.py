from django.db import models
from django.utils import timezone
# from user_management.models import UserAccount
from apps.user_management.models import UserAccount

# Create your models here.
class Blog(models.Model):
    
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField()
    media = models.ImageField(upload_to='media/blog_imgs',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    isReported = models.BooleanField(null=False,default=True)

    def __str__(self):
        return self.user.email

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    user = models.ForeignKey(UserAccount,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.CharField(max_length=150,null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
