"""Blog admin."""

# Django
from django.contrib import admin

# Custom
from .models import Post

class PostAdmin(admin.ModelAdmin):
    """
    Content displayed about each Post in the admin site.
    """

    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
