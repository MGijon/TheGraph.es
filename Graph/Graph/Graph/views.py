"""Graph views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
# from django.urls import reverse_lazy      # not used now
from django.shortcuts import render


def index(request):
    """
    """
    print('entra')

    template_name = 'index.html'

    return render(request, template_name)
