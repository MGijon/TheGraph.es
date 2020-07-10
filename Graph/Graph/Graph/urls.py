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
    # Blog urls
    path(route = '',
         view = include(('blog.urls', 'blog')),
         name = 'blog'),
    # Projects urls
    path(route='',
         view = include(('projects.urls', 'projects')),
         name='projects'),
    # Users
    path(route='',
         view = include(('users.urls', 'users')),
         name = 'users'),
]
