from django.db import models

class Blog(models.Model):
    # user_id =
    # temp_username = models.CharField(max_length=60)
    post_msg = models.TextField()
    date_added = models.DateField(auto_now=True)
    media = models.ImageField()
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.post_msg
