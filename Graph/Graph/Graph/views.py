"""Graph views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render


def index(request):
    """Return index.html template."""
    template_name = 'index.html'

    return render(request, template_name)

def about(request):
    """Return about template."""
    template_name = 'about.html'

    return render(request, template_name)
