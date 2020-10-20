# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
#from post.models import Post
from django.db.models.signals import post_save

# Create your models here.
created = models.DateTimeField(auto_now_add=True)
class Profile(models.Model):

    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=1)
    bio = models.TextField(max_length=300, default="no bio...")
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    profile_desc = models.TextField(max_length=150,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='profile_pictures', default="avatar.png")
    friends = models.ManyToManyField(User, blank=True, related_name='friends')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.user.username}{self.created}"

    def create_profile(self):
        profile = Profile.objects.all()
        profile.save()

    def delete_profile(self, pk):
        deleted_profile = Profile.objects.get(pk)
        deleted_profile.delete()


class Image(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True)
    image_name = models.CharField(null=True, max_length=60)
    image_caption = models.CharField(null=True, max_length=100)
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    likes = models.BooleanField(null=True, rel='likes')
    comments = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        saved_image = Image.objects.all()
        saved_image.save()

    def delete_image(self, pk):
        delete_image = Image.objects.get(pk)
        delete_image.delete()

    def update_caption(self, caption):
        cap = Image.objects.all(caption)
        cap.save()

    def search(request):
        if request.method == 'POST':
            user_name = request.POST.getlist('search')
            try:
                status = Image.objects.filter(username__icontains=user_name)
                # Add_prod class contains a column called 'user_name'
            except Image.DoesNotExist:
                status = None
            return render(request, "search.html", {"user": status})
        else:
            return render(request, "search.html", {})