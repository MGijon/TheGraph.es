"""Projects views."""

# Django
from django.views import generic

# Project models
from .models import Project

class ProjectsList(generic.ListView):
    """Post list view."""
    #queryset = Project.objects.filter(status=1).order_by('-created_on')
    queryset = Project.objects.order_by('-project_created_on')
    template_name = 'projects/feed_projects.html'

class ProjectDetail(generic.DetailView):
    """Project detail view."""
    model = Project
    template_name = 'projects/project_detail.html'
