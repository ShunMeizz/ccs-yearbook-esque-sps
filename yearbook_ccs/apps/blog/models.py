from django.db import models
from django.utils import timezone
# from user_management.models import UserAccount
from apps.user_management.models import UserAccount

# Create your models here.
class Blog(models.Model):
    
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,blank=True, related_name="user")
    title = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField()
    media = models.ImageField(upload_to='media/blog_imgs',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    isReported = models.BooleanField(null=False,default=True)

    def __str__(self):
        return self.user.email