"""Projects urls."""

from django.urls import path

# Blog views
from projects import views

urlpatterns = [
    # Projects feed
    path(route = 'projects/',
		 view = views.ProjectsList.as_view(),
		 name = 'feed'),
]
