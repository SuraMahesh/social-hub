from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from urllib.parse import urldefrag
from django.db import models
from django.contrib.auth.models import User
from numpy import blackman

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    logo = models.ImageField(default='', upload_to='', blank=True, null=True)
   


    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(default='', upload_to='', blank=True, null=True)
    name = models.CharField(max_length=200, null=True, blank=True, default='TEST')
    socials = models.ManyToManyField('Social', blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

class Post(models.Model):
    OPTIONS = (
        ('college', 'college'),
        ('job', 'job'), 
        ('default', 'default')
    )
    
    owner = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    body = models.TextField(max_length=500, blank=True)  
    created = models.DateTimeField(auto_now_add=True)    
    post_type = models.CharField(choices=OPTIONS, default=OPTIONS[2], max_length=500)
    like = models.ManyToManyField(User, related_name='like', blank=True)

    def __str__(self):
        return self.body[0:50]


class Social(models.Model):
    icon = models.ImageField(default='', upload_to='', blank=True, null=True)
    link = models.URLField(max_length=200)


class Skill(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True) 


class Comment(models.Model):
    owner = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, models.CASCADE, blank=True, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)  
   
    

    def __str__(self):
        return self.body[0:50]

# class Like(models.Model):
#     owner = models.ForeignKey(User, models.CASCADE, blank=True, null=True)

