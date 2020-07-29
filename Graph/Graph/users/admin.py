"""Users admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from django.contrib.auth.models import User
from users.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    # Campos que se mostrarán en el panel de administración
    list_display = ('profile_user',)#'pk', 'user', 'phone_number', 'website', 'picture')

    # Al pulsar sobre estos nos llevarán al detalle
    list_display_links = ()#'pk', 'phone_number')

    # Campos editables con un click
    list_aditable = ('picture')

    # self-explanatory
    search_fields = ('user_email', 'user_first_name', 'user_last_name', 'phone_number')

    # Campos por los que podremos filtrar
    list_filter = ()#'user_is_active', 'user__is_staff')

    fieldsets = (('Profile', { 'fields': ( ('profile_user', 'profile_picture'), ), }),
                 ('Extra info', {'fields': (
                                    ('profile_website', 'profile_phone_number'),
                                    ('profile_biography'), ),
                                }),)

class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for user."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInLine, )
    list_display = ('username', 'email')  ## TODO:

# Sustituímos un modelo por otro
admin.site.unregister(User)
# Recibe modelo y clase que vamos a utilizar
admin.site.register(User, UserAdmin)
