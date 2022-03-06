from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    path('home/',views.index,name='home'),
    path('', views.login_user, name='login'),
    path('register/', views.register, name='register')
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)