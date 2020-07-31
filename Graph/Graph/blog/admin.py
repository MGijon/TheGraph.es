"""Blog admin."""

# Django
from django.contrib import admin

# Custom
from .models import Post

class PostAdmin(admin.ModelAdmin):
    """
    Content displayed about each Post in the admin site.
    """

    list_display = ('post_title',
                    'slug',
                    'post_status',
                    'post_created_on')

    list_filter = ('post_status',)

    search_fields = ['post_title', 'post_content']

    prepopulated_fields = {'slug': ('post_title',)}

admin.site.register(Post, PostAdmin)
