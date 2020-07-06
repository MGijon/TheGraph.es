"""Projects models."""

# Django
from django.db import models
from django.contrib.auth.models import User

# TODO: adapt this in the future
STATUS = (
    (0, "Secret"),
    (1, "Open"),
    (2, "Closed"),
)

class Project(models.Model):
    """Project model.

    :title: self-explanatory.
    :slug: reference to the url of the project front-page.
    :author: self-explanatory.
    :collaborator_1: self-explanatory.
    :collaborator_2: self-explanatory.
    :abstract: self-explanatory.
    :status: self-explanatory.
    :created_on: self-explanatory.
    :closed_on: self-explanatory.
    :description: long description of the model (despite the things added on
                  the template).
    :key_word_1: self-explanatory.
    :key_word_2: self-explanatory.
    :key_word_3: self-explanatory.
    :key_word_4: self-explanatory.
    :key_word_5: self-explanatory.
    :description_link_1: text linked to the 'link_1' direction.
    :description_link_2: text linked to the 'link_1' direction.
    :description_link_3: text linked to the 'link_1' direction.
    :description_link_4: text linked to the 'link_1' direction.
    :description_link_5: text linked to the 'link_1' direction.
    :link_1: self-explanatory.
    :link_2: self-explanatory.
    :link_3: self-explanatory.
    :link_4: self-explanatory.
    :link_5: self-explanatory.
    :miniature: image, a miniature for the project.   
    """
    # Title and slug name (used in the url)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # Authors
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    collaborator_1 = models.CharField(max_length=100, blank=True)
    collaborator_2 = models.CharField(max_length=100, blank=True)
    # Abstract (fot the preview) and description (for the detail view)
    abstract = models.TextField()
    description = models.TextField()
    # Status and timestamps
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    closed_on = models.DateTimeField(blank=True)
    # Key words (for tagging propouses)
    key_word_1 = models.CharField(max_length=75)
    key_word_2 = models.CharField(max_length=75, blank=True)
    key_word_3 = models.CharField(max_length=75, blank=True)
    key_word_4 = models.CharField(max_length=75, blank=True)
    key_word_5 = models.CharField(max_length=75, blank=True)
    # Links (to urls) and their descriptions (text linked)
    description_link_1 = models.CharField(max_length=150, blank=True)  # luego será necesario
    description_link_2 = models.CharField(max_length=150, blank=True)
    description_link_3 = models.CharField(max_length=150, blank=True)
    description_link_4 = models.CharField(max_length=150, blank=True)
    description_link_5 = models.CharField(max_length=150, blank=True)
    link_1 = models.CharField(max_length=150, blank=True)  # luego será necesario
    link_2 = models.CharField(max_length=150, blank=True)
    link_3 = models.CharField(max_length=150, blank=True)
    link_4 = models.CharField(max_length=150, blank=True)
    link_5 = models.CharField(max_length=150, blank=True)
    # Miniature for the preview
    miniature = models.ImageField(
        upload_to = 'projects/',
        blank = True,
        null = True,
    )
    # Images
    image_1 = models.ImageField(
        upload_to = 'projects/',
        blank = True,
        null = True,
    )
    image_2 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    image_3 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    image_4 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    image_5 = models.ImageField(upload_to = 'projects/', blank = True, null = True)



    class Meta:
        """TODO: description of this."""
        ordering = ['-created_on']

    def __str__(self):
        """Information about the Project model.
        TODO: IMPROVE THIS!!
        """
        return self.title
