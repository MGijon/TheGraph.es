"""Graph urls."""

# Django
from django.contrib import admin
from django.urls import path

# Graph
from .views import * # let's see if that works

urlpatterns = [
    path('admin/', admin.site.urls),
    # Blog urls
    path(route = '',
         view = index,
         name = 'index')
]
