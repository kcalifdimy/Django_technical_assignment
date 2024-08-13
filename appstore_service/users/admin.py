from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from .models import User

# Custom admin interface for the User model.
# - Extends Django's default UserAdmin to customize the user management
# interface in the admin panel.


class MyUserAdmin(auth_admin.UserAdmin):
    model = User  # Specifies the User model to be managed by this admin class

    # Fieldsets define the layout and fields for the user detail view 
    # in the admin interface
    fieldsets = (
        # Fields for email and password
        (None, {"fields": ("email", "password")}),
        # Fields for personal information
        (_("Personal info"), {"fields": ("first_name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),  # Fields for user permissions and roles
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    # Fieldsets for the user creation form in the admin interface
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2"
                ),  
            },
        ),
    )

    # Fields to be displayed in the user list view in the admin panel
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_superuser"
    ]

    # Fields to be used for searching users in the admin panel
    search_fields = ["first_name"]
    # Default ordering of user instances in the admin panel
    ordering = ["id"]


# Register the User model with the custom MyUserAdmin configuration in the Django admin site
admin.site.register(User, MyUserAdmin)
