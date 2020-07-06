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
    # Title and slug name (used in the url)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # Authors
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    #collaborator_1 = models.ForeignKey(User, default='Null', on_delete = models.CASCADE, blank=True)
    # Contente
    content = models.TextField()
    # Status and timestamps
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    # Images
    image_1 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    image_2 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    image_3 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    image_4 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    image_5 = models.ImageField(upload_to = 'projects/', blank = True, null = True)


    class Meta:
        """TODO: descriptoin of this."""
        ordering = ['-created_on']

    def __str__(self):
        """Information to return about the Post model."""
        return self.title
