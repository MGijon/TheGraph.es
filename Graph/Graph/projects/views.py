"""Projects views."""

# Django
from django.views import generic

from .models import Project
'''
from django.template.response import TemplateResponse

def temporal_function(request):
    """Temporal, just return the template."""
    print('\nEntra en esta función temporal ad-hoc\n')
    return TemplateResponse(request, 'about.html')  #projects/feed_projects.html')

'''
class ProjectsList(generic.ListView):
    """Post list view."""
    print('\nentra en la función ProjectsList\n')
    queryset = Project.objects.filter(status=1).order_by('-created_on')
    template_name = 'projects/feed_projects.html'
