from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
# Create your models here.





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()





class Relationship(models.Model):
    type = models.TextField(max_length=50,blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class People(models.Model):
    friend_id=models.PositiveIntegerField(null=True, blank=True)
    rel_id= models.ForeignKey(Relationship,on_delete=models.CASCADE)
