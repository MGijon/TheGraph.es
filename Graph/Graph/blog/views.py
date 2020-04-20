"""Blog views."""

# Django
from django.shortcuts import render
from django.views import generic

# Post models
from .models import Post

class PostList(generic.ListView):
    """Post list view."""
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    """Post detail view."""
    model = Post
    template_name = 'post_detail.html'
