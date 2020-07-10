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

    :project_id: sefl-explanatory.

    :project_title: self-explanatory.
    :project_slug: reference to the url of the project front-page.

    :project_author: self-explanatory.
    :project_collaborator_1: self-explanatory.
    :project_collaborator_2: self-explanatory.

    :project_abstract: self-explanatory.
    :project_description: long description of the model (despite the things added on
                          the template).

    :project_status: self-explanatory.
    :project_created_on: self-explanatory.
    :project_closed_on: self-explanatory.

    :project_key_word_1: self-explanatory.
    :project_key_word_2: self-explanatory.
    :project_key_word_3: self-explanatory.
    :project_key_word_4: self-explanatory.
    :project_key_word_5: self-explanatory.

    :project_description_link_1: text linked to the 'link_1' direction.
    :project_description_link_2: text linked to the 'link_1' direction.
    :project_description_link_3: text linked to the 'link_1' direction.
    :project_description_link_4: text linked to the 'link_1' direction.
    :project_description_link_5: text linked to the 'link_1' direction.
    :project_link_1: self-explanatory.
    :project_link_2: self-explanatory.
    :project_link_3: self-explanatory.
    :project_link_4: self-explanatory.
    :project_link_5: self-explanatory.

    :project_miniature: image, a miniature for the project.
    :project_image_1: self-explanatory.
    :project_image_2: self-explanatory.
    :project_image_3: self-explanatory.
    :project_image_4: self-explanatory.
    :project_image_5: self-explanatory.
    """
    # Project id
    project_id = models.AutoField(primary_key = True)
    # Title and slug name (used in the url)
    project_title = models.CharField(max_length=200, unique=True)
    project_slug = models.SlugField(max_length=200, unique=True)
    # Authors
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    project_collaborator_1 = models.CharField(max_length=100, blank=True)
    project_collaborator_2 = models.CharField(max_length=100, blank=True)
    # Abstract (fot the preview) and description (for the detail view)
    project_abstract = models.TextField()
    project_description = models.TextField()
    # Status and timestamps
    project_status = models.IntegerField(choices=STATUS, default=0)
    project_created_on = models.DateTimeField(auto_now_add=True)
    # Añadir el updated on
    project_closed_on = models.DateTimeField(blank=True)
    # Key words (for tagging propouses)
    project_key_word_1 = models.CharField(max_length=75)
    project_key_word_2 = models.CharField(max_length=75, blank=True)
    project_key_word_3 = models.CharField(max_length=75, blank=True)
    project_key_word_4 = models.CharField(max_length=75, blank=True)
    project_key_word_5 = models.CharField(max_length=75, blank=True)
    # Links (to urls) and their descriptions (text linked)
    project_description_link_1 = models.CharField(max_length=150, blank=True)  # luego será necesario
    project_description_link_2 = models.CharField(max_length=150, blank=True)
    project_description_link_3 = models.CharField(max_length=150, blank=True)
    project_description_link_4 = models.CharField(max_length=150, blank=True)
    project_description_link_5 = models.CharField(max_length=150, blank=True)
    project_link_1 = models.CharField(max_length=150, blank=True)  # luego será necesario
    project_link_2 = models.CharField(max_length=150, blank=True)
    project_link_3 = models.CharField(max_length=150, blank=True)
    project_link_4 = models.CharField(max_length=150, blank=True)
    project_link_5 = models.CharField(max_length=150, blank=True)
    # Miniature for the preview
    project_miniature = models.ImageField(
        upload_to = 'projects/',
        blank = True,
        null = True,
    )
    # Images
    project_image_1 = models.ImageField(
        upload_to = 'projects/',
        blank = True,
        null = True,
    )
    project_image_2 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    project_image_3 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    project_image_4 = models.ImageField(upload_to = 'projects/', blank = True, null = True)
    project_image_5 = models.ImageField(upload_to = 'projects/', blank = True, null = True)



    class Meta:
        """TODO: description of this."""
        ordering = ['-project_created_on']

    def __str__(self):
        """Information about the Project model.
        TODO: IMPROVE THIS!!
        """
        return self.project_title
