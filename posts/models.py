from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author= models.ForeignKey('auth.User',on_delete=models.CASCADE)
    image= models.ImageField(blank=True,null=True)
    image_caption= models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.image_caption
     
