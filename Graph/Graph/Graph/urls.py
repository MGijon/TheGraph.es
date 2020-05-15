"""Graph urls."""

# Django
from django.contrib import admin
from django.urls import path, include

# Graph
from .views import * # let's see if that works

urlpatterns = [
    path('admin/', admin.site.urls),
    # General
    path(route = '',
         view = index,
         name = 'index'),
    path(route = 'about/',
         view = about,
         name = 'about'),
    # Blog urls
    path(route = '',
         view = include(('blog.urls', 'blog')),
         name = 'blog'),
    # Projects urls
    path(route='',
         view = include(('projects.urls', 'projects')),
         name='projects'),
]
