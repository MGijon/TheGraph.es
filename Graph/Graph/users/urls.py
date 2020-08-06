"""Users Urls."""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    # login
    path(route='users/login/',
         view=views.LoginView.as_view(),
         name='login'),
    # logout
    path(route='users/logout',
         view=views.LogoutView.as_view(),
         name='logout'),
    # signup
    path(route='users/signup',
         view=views.SignupView.as_view(),
         name='signup'),
    # update
    path(route='users/me/profile/',
         view=views.UpdateProfileView.as_view(),
         name='update_profile'),
    # posts
    path(route='<str:username>',
         view=views.UserDetailView.as_view(),
         name='detail')
]


"""
BAD_CODE:
=========

path(route = 'users/me/profile', view = views.UpdateProfileView.as_view(), name = 'update_profile'),

"""
