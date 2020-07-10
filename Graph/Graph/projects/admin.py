"""Projects admin."""

# Django
from django.contrib import admin

# Custom
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    """
    Content displayed about each Project in the admin site.
    """

    list_display = ('project_title',
                    'project_slug',
                    'project_status',
                    'project_created_on', )
    list_filter = ('project_status',)
    search_fields = ['project_title',]    # TODO: end this, just wanna know that works
    prepopulated_fields = {
        'project_slug': ('project_title',),
    }

admin.site.register(Project, ProjectAdmin)
