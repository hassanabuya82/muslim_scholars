from django.db import models
from myauth.models import CustomUser
from pathlib import Path

# Create your models here.


def post_pics(instance, filename):
    return Path(f'post_pics')/filename

class Post(models.Model):
    picture = models.ImageField(upload_to=post_pics, blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='posts', null=True)

    def __str__(self):
        return self.title

    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'