from cloudinary.models import CloudinaryField
from distutils.command.upload import upload
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author= models.ForeignKey('auth.User',on_delete=models.CASCADE,null=True)
    image = CloudinaryField('image')
    image_caption= models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.image_caption
     
class Comments(models.Model):
    post=models.ForeignKey('Post',related_name='comment',on_delete=models.CASCADE,blank=True)
    name= models.CharField(max_length=30)
    body= models.CharField(max_length=30)
    date_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return '%s-%s' %(self.post.author,self.name)