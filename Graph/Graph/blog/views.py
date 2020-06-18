"""Blog views."""

# Django
from django.views import generic

# Post models
from .models import Post

class PostList(generic.ListView):
    """Post list view."""
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/feed.html'

class PostDetail(generic.DetailView):
    """Post detail view."""
    model = Post
    '''
    try:
        template_name = 'blog/post_detail.html'
    except:
        pass
    '''
    template_name = 'blog/post_detail.html'
