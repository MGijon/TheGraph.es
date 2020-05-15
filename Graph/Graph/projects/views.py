"""Projects views."""

# Django
from django.views import generic

class ProjectsList(generic.ListView):
    """Post list view."""
    print('DAME ALEGRÍA PA MI CUERPO!!!!')

    template_name = 'projects/feed_projects.html'
