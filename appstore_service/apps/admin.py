from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from appstore_service.apps.models import App


class AppAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the App model.This class customizes 
    how App instances are displayed and managed in the Django admin panel.
    """

    # Fields to be displayed in the list view of the admin panel.
    # - 'owner': The owner of the app.
    # - 'title': The title of the app.
    # - 'icon': The icon representing the app.
    # - 'description': A brief description of the app.
    # - 'verified': Indicates whether the app is verified.
    # - 'price': The price of the app.
    # - 'created_at': The timestamp when the app was created.

    list_display = (
        'owner',
        'title',
        'icon',
        'description',
        'verified',
        'price',
        'created_at',
    )
    # Fields that can be edited directly in the list view.
    list_editable = (
        'title',
        'icon',
        'description',
        'verified',
        'price',
    )
 
    # Override the default queryset to order the App instances by 'owner'.
    def get_queryset(self, request):
        queryset = super(AppAdmin, self).get_queryset(request)
        queryset = queryset.order_by('owner')
        return queryset

# Register the App model with the custom AppAdmin configuration in the Django 
# admin site.
# - This makes the App model manageable via the Django admin interface with 
# the specified customizations.


admin.site.register(App, AppAdmin)
