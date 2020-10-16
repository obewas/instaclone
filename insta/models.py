# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from post.models import Post
from django.db.models.signals import post_save

# Create your models here.
created = models.DateTimeField(auto_now_add=True)
class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,null=True, blank=True)
    last_name = models.CharField(max_length=30,null=True, blank=True)
    location = models.CharField(max_length=30,null=True, blank=True)
    url = models.CharField(max_length=100,null=True, blank=True)
    profile_desc = models.TextField(max_length=150,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #favorites = models.ManyToManyField(Post)
    picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True, verbose_name='pic')

def create_user_profile(sender, instance, **kwargs):
    if created:
        Profile.objects.create(User=instance)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)