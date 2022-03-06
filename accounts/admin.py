from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Comments, Images, Likes, User

# Register your models here.
admin.site.register(User)
admin.site.register(Images)
admin.site.register(Likes)
admin.site.register(Comments)