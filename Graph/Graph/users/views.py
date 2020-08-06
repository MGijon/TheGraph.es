"""Users Views."""

# Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import SignupForm #, ProfileForm

class LoginView(auth_views.LoginView):
    """TODO:description"""
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
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

#### NEW THIGS TO TEST ####
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['profile_biography',]

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username', username})

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name='users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()

    context_object_name = 'user'


    ######## REPARAR ESTO; LOS Términos son literales de otro proyecto #########
    def get_contect_data(self, **kwargs):
        """Add user's posts to context."""
        contect = super().get_context_data(**kwargs)
        user=self.get_object()
        context['posts'] = Posts.objects.filter(user=user).order_by('-created')
        return context
