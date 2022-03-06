from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class Images(models.Model):
    user=models.ForeignKey('User',on_delete=models.CASCADE,blank=True)
    image= models.ImageField()
    image_name= models.CharField(max_length=50)
    image_caption= models.CharField(max_length=50)
    
    def __str__(self):
        return self.image_name
    
    
class Likes(models.Model):
    user=models.ForeignKey('User',on_delete=models.CASCADE,blank=True)
    images= models.ForeignKey('Images',on_delete=models.CASCADE,blank=True)
    likes= models.CharField(max_length=30)
    
    def __str__(self):
        return self.likes

class Comments(models.Model):
    user=models.ForeignKey('User',on_delete=models.CASCADE,blank=True)
    images= models.ForeignKey('Images',on_delete=models.CASCADE,blank=True)
    comments= models.CharField(max_length=30)
    
    def __str__(self):
        return self.comments
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
# User authetification models here.
class Account(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        user = self.model(
            first_name, 
            last_name,
            username,
            email
        )
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email = email,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using = self._db)

        return user
        


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(unique=True, max_length=200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = Account()

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    # super user properties
    is_admin = models.BooleanField(False)
    is_staff = models.BooleanField(False)
    is_active = models.BooleanField(False)
    is_superuser = models.BooleanField(False)
