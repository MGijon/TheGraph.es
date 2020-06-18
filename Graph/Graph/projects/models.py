"""Projects urls."""

# Django
from django.db import models
from django.contrib.auth.models import User

# TODO: adapt this in the future
STATUS = (
    (0, "Open"),
    (1, "Closed")
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
    :link_1: self-explanatory.
    :link_2: self-explanatory.
    :link_3: self-explanatory.
    :link_4: self-explanatory.
    :link_5: self-explanatory.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    collaborator_1 = models.CharField(max_length=100)
    collaborator_2 = models.CharField(max_length=100)
    abstract = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    closed_on = models.DateTimeField()
    description = models.TextField()
    key_word_1 = models.CharField(max_length=75)
    key_word_2 = models.CharField(max_length=75)
    key_word_3 = models.CharField(max_length=75)
    key_word_4 = models.CharField(max_length=75)
    key_word_5 = models.CharField(max_length=75)
    link_1 = models.CharField(max_length=150)
    link_2 = models.CharField(max_length=150)
    link_3 = models.CharField(max_length=150)
    link_4 = models.CharField(max_length=150)
    link_5 = models.CharField(max_length=150)


    class Meta:
        """TODO: description of this."""
        ordering = ['-created_on']

    def __str__(self):
        """Information about the Project model.
        TODO: IMPROVE THIS!!
        """
        return self.title
