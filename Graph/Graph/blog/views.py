"""Blog views."""

# Django
from django.shortcuts import render
from django.views import generic

# Post models
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/feed.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
