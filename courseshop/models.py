from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
class extendeduser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_num = models.CharField(max_length = 15)
    dob = models.CharField(max_length = 15,default="")
    addre = models.CharField(max_length = 500)
@receiver(post_save, sender=User)
# def create_user_profile(sender, instance=None, created=False, **kwargs):
#     if created:
#         profile = extendeduser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = extendeduser(user=user)
class Order(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=13)
    address= models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    timeStamp=models.DateTimeField(auto_now_add=True)
    user1 = models.ForeignKey(User,on_delete=models.CASCADE)
