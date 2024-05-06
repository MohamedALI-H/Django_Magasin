from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_on']

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = 'blog/'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'status', 'image']
    template_name = 'blog/post_update.html'
    success_url = '/blog/'
    context_object_name = 'post'
    

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
