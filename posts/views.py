from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from .models import Post
from .forms import PostForm

from django.views.generic import (ListView,CreateView,DetailView, UpdateView,DeleteView)
from django.utils import timezone

# Create your views here.

class PostListView(ListView):
    template_name= 'posts/post.html'
    queryset= Post.objects.all().filter(created_at__lte=timezone.now()).order_by('-created_at')
    context_object_name='posts'

class PostCreateView(CreateView):
    template_name='posts/post_create.html'
    form_class= PostForm
    queryset= Post.objects.all()
    success_url='/'
    
    def form_isvalid(self,form):
        print(form.cleaned_data)
        form.instance.author=self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    template_name= 'posts/detail.html'
    queryset=Post.objects.all().filter(created_at__lte=timezone.now())
    def get_object(self):
        id=self.kwargs.get('id')
        return get_object_or_404(Post,id=id)
class PostUpdateView(UpdateView):
    template_name = 'posts/post_create.html'
    form_class = PostForm 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form) 

class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse('posts:postlist')