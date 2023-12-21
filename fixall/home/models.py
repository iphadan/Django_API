from typing import Any
from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import os
@deconstructible
class GenerateProfilePath(object):
    def __init__(self):
        ...
    def __call__(self, instance,filename):
        ext=filename.split('.')[-1]
        path='media/accounts/profiles/'
        name=f'profile_img_{instance.user.id}.{ext}'

        return os.path.join(path,name)
        
# Create your models here.
user_profile_img_path=GenerateProfilePath()
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    img=models.FileField(upload_to=user_profile_img_path,blank=True,null=True)
    def __str__(self):
        return f'{self.user.username}'
