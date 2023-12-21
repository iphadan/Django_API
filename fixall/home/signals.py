from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from . import models
import random

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created :
        models.Profile.objects.create(user=instance)
        print(sender)


@receiver(pre_save,sender=User)
def create_usename(sender,instance,**kwargs):
    username=f'{instance.first_name}.{instance.last_name}'.lower()
    users_with_username=User.objects.filter(username=username)
    while True and len(users_with_username) != 0:
        count=random.randint(0,10000000)
        username=f'{instance.first_name}{instance.last_name}{count}'.lower()
        
        users_with_username=User.objects.filter(username=username)
    
    

  
    instance.username=username 