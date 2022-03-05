from django.db import models

# Create your models here.
class Images(models.Model):
    user=models.ForeignKey('User',on_delete=models.CASCADE,blank=True)
    image= models.ImageField()
    image_name= models.CharField(max_length=50)
    image_caption= models.CharField(max_length=50)
    
    def __str__(self):
        return self.image
    
    
class Likes(models.Model):
    user=models.ForeignKey('Users',on_delete=models.CASCADE,blank=True)
    images= models.ForeignKey('Images',on_delete=models.CASCADE,blank=True)
    likes= models.CharField(max_length=30)
    
    def __str__(self):
        return self.likes

class Comments(models.Model):
    user=models.ForeignKey('Users',on_delete=models.CASCADE,blank=True)
    images= models.ForeignKey('Images',on_delete=models.CASCADE,blank=True)
    comments= models.CharField(max_length=30)
    
    def __str__(self):
        return self.comments