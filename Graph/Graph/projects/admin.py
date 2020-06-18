"""Projects admin."""

# Django
from django.contrib import admin

# Custom
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    """
    Content displayed about each Project in the admin site.
    """

    list_display = ('title', 'slug', 'status', 'created_on', )
    list_filter = ('status',)
    search_fields = ['title',]    # TODO: end this, just wanna know that works
    prepopulated_fields = {
        'slug': ('title',),
    }

admin.site.register(Project, ProjectAdmin)
