"""Blog views."""

# Django
from django.views import generic

# Post models
from .models import Post

class PostList(generic.ListView):
    """Post list view."""
    queryset = Post.objects.filter(post_status=1).order_by('-post_created_on')
    template_name = 'blog/feed.html'

class PostDetail(generic.DetailView):
    """Post detail view."""
    model = Post
    template_name = 'blog/post_detail.html'
