from django.db import models
from apps.profiles.models import UserProfile
from apps.user_management.models import UserAccount
# from apps.blog.models import Blog 

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date_created} : {self.author.username} commented {self.comment}"
    
class ProfileComment(Comment):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile_comments')

    def __str__(self):
        return super().__str__() + f" on the Profile: {self.profile.user_account.username}"

class BlogComment(Comment):
    # blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments')

    def __str__(self):
        return super().__str__() + f" on the Blog: "