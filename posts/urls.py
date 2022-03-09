from django.urls import path,include,reverse
from django.urls import reverse_lazy

from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    
)
app_name= 'posts'

urlpatterns=[
    
    path('post/',PostListView.as_view(),name='postlist'),
    # path('post/',PostListView.as_view(success_url=reverse_lazy('posts:postlist'), template_name="posts/posts.html"), 
    #     name="postlist"),

    path('new/',PostCreateView.as_view(),name='post_create'),
    path('<int:id>/',PostDetailView.as_view(),name='post_detail'),
]