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

    :post_id: self-explanatory.

    :post_title: self-explanatory.
    :post_slug: reference to the url of the post.

    :post_author: self-explanatory.

    :post_content: self-explanatory.

    :post_status: self-explanatory.
    :post_created_on: self-explanatory.
    :post_updated_on: self-explanatory.

    :post_key_word_1: self-explanatory.
    :post_key_word_2: self-explanatory.
    :post_key_word_3: self-explanatory.

    :post_image_1: self-explanatory.
    :post_image_2: self-explanatory.
    :post_image_3: self-explanatory.
    :post_image_4: self-explanatory.
    :post_image_5: self-explanatory.
    """
    # Id
    post_id = models.AutoField(primary_key = True)
    # Title and slug name (used in the url)
    post_title = models.CharField(max_length=200, unique=True)
    post_slug = models.SlugField(max_length=200, unique=True)
    # Authors
    post_author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts')
    #collaborator_1 = models.ForeignKey(User, default='Null', on_delete = models.CASCADE, blank=True)
    # Contente
    post_content = models.TextField()
    # Status and timestamps
    post_status = models.IntegerField(choices=STATUS, default=0)
    post_created_on = models.DateTimeField(auto_now_add=True)
    post_updated_on = models.DateTimeField(auto_now= True)
    # Key words (for tagging propouses)
    post_key_word_1 = models.CharField(max_length=75, default='Artificial Intelligence')
    post_key_word_2 = models.CharField(max_length=75, blank=True)
    post_key_word_3 = models.CharField(max_length=75, blank=True)
    # Images
    post_image_1 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    post_image_2 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    post_image_3 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    post_image_4 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    post_image_5 = models.ImageField(upload_to = 'projects/', blank = True, null = True)


    class Meta:
        """TODO: description of this."""
        ordering = ['-post_created_on']

    def __str__(self):
        """Information to return about the Post model."""
        return self.title
