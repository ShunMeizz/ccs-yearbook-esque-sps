from django.db import models
from django.utils import timezone
# from user_management.models import UserAccount
from apps.user_management.models import UserAccount

# Create your models here.
class Blog(models.Model):
    # username = models.CharField(max_length=30,default="Test")
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField()
    media = models.ImageField(upload_to='media/blog_imgs',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
    
    # def test(query):
    #     return Blog.objects.filter(query)
    
