"""Users Views."""

# Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import loginRequiredMixin
from django views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views

# Models
from django.contrib.auth.models import User
from users.models import Profile

class LoginView(auth_views.LoginView):
    """TODO:description"""
    template_name = 'user/login.html'

class LogoutView(loginRequiredMixin, auth_views.LogoutView):
    """TODO:description."""
    template_name = 'users/logged_out.html'

class SignupView(FormView):
    """TODO:description"""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """TODO: description."""
        form.save()
        return super().form_valid(form)
