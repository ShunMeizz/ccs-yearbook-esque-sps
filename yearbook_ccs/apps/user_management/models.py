from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.



class UserAccount(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(null=True)
    school_id_number = models.CharField(max_length=50, null=True)
    id_front = models.ImageField(upload_to='media/id_images/front', null=True, blank=True)
    id_back = models.ImageField(upload_to='media/id_images/back', null=True, blank=True)
    photo_w_id = models.ImageField(upload_to='media/id_images/photo', null=True, blank = True)
    is_acc_verified = models.BooleanField(default=False)


    REQUIRED_FIELDS = ['email']
    def __str__(self):
        return self.email if self.email else "No Email"



