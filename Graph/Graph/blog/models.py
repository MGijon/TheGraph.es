"""Blog models."""

# Django
from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    """Post model.

    :title: self-explanatory.
    :slug: reference to the url of the post.
    :author: self-explanatory.
    :updated_on: self-explanatory.
    :content: self-explanatory.
    :created_on: self-explanatory.
    :status: self-explanatory.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
