from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(is_active=True)
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post_list.html'


