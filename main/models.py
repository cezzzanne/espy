from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    profile_image = models.ImageField(upload_to='profile_pictures', blank=True)


class Image(models.Model):
    image = models.ImageField(upload_to='user_images', blank=False)
    caption = models.TextField(max_length=140, null=True)


class Comment(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField(max_length=200, blank=False)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comment')
