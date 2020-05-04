"""Blog urls."""

# Django
from django.urls import path

# Blog views
from blog import views

urlpatterns = [
    path(route = '',
		 view = views.PostList.as_view(),
		 name ='feed'),
]
