"""Blog urls."""

# Django
from django.urls import path

# Blog views
from blog import views

urlpatterns = [
    # Blog feed
    path(route = 'feed/',
		 view = views.PostList.as_view(),
		 name = 'feed'),
    # For post details
    path(route = '<slug:slug>/',
         view = views.PostDetail.as_view(),
         name = 'post_detail'),
]
