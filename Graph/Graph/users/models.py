"""Users Models."""

# Django
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile extended:
    Proxy model that extends the base data with other information.
    """
    # this links Profile with the User profile, one to one relationship
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Website filed
    profile_website = models.URLField(max_length=200, blank=True)
    # Biography
    profile_biography = models.TextField(blank=True)
    # Phone number
    profile_phone_number = models.CharField(max_length=20, blank=True)
    # Picture
    profile_picture = models.ImageField(
        upload_to = 'users/pictures',
        blank = True,
        null = True,)
        
    profile_created_on = models.DateTimeField(auto_now_add = True)
    profile_modified_on = models.DateTimeField(auto_now = True)


    def __str__(self):
        """TODO: description."""
        return self.profile_user.username
