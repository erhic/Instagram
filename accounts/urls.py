from django.urls import path
from . import views


urlpatterns=[
    path('post/',views.login,name='post'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register')
    
    ]