from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    profile_user=models.OneToOneField(User, on_delete=models.CASCADE )
    profile_img=models.ImageField(upload_to='profileImage',default='profileImage/userAvatar.png')
    bio=models.CharField(blank=True, max_length=500)
    verify=models.BooleanField(default=False)


    def __str__(self):
        return str(self.profile_user)
    pass
