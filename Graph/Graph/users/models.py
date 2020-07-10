"""Users Models."""

# Django
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile extended:
    Proxy model that extends the base data with other information.
    """

    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_website = models.URLField(max_length=200, blank=True)
    profile_biography = models.TextField(blank=True)

    profile_phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(
        upload_to = 'users/pictures',
        blank = True,
        null = True,)
    profile_created_on = models.DateTimeField(auto_now_add = True)
    profile_modified_on = models.DateTimeField(auto_now = True)


    def __str__(self):
        """TODO: description."""
        return self.profile_user.username
