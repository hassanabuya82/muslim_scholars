from django.db import models
from myauth.models import CustomUser
from pathlib import Path

# Create your models here.


def post_pics(instance, filename):
    return Path(f'post_pics')/filename

class Post(models.Model):
    image = models.ImageField(upload_to=post_pics, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    reading_time = models.CharField(max_length=255,null=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts', null=True)

    def __str__(self):
        return self.title

    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class ContactEmail(models.Model):
    email = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(null=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

class ContactUs(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=1000, null=True)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
