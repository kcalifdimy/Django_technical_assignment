from django.urls import path

from appstore_service.apps.api import views

# Define the app name for namespacing the URLs.
# - This allows the URLs to be referenced unambiguously when using Django's
# reverse URL lookup.

app_name = "apps"

# URL patterns for the App API endpoints.
# - These URLs map to specific views in the appstore_service.apps.api.views
# module.

urlpatterns = [
    # URL pattern for creating a new app.
    # - Maps to the AppCreateView, which handles the creation of App instances.
    # - The URL is 'create' and is named 'app-create' for easy reference.

    path('create',
         views.AppCreateView.as_view(),
         name='app-create'
         ),

    # URL pattern for listing all verified apps.
    # - Maps to the AppListView, which provides a list of all verified App 
    # instances.
    # - The URL is 'list' and is named 'app-list' for easy reference.

    path('list',
         views.AppListView.as_view(),
         name='app-list'
         ),

    # URL pattern for searching apps by title or description.
    # - Maps to the SerachView, which allows searching within the verified
    # apps.
    # - The URL is 'search' and is named 'app-list' for easy reference (should
    # be 'app-search' for clarity).

    path('search',
         views.SerachView.as_view(),
         name='app-search'
         ),

    # URL pattern for retrieving, updating, or deleting a specific app by its
    # primary key (pk).
    # - Maps to the AppRetrieveUpdateDestroyAPIViews, which handles these
    # operations for a single App instance.
    # - The URL is 'details/<int:pk>/' and is named 'app-detail' for easy
    # reference.

    path('details/<int:pk>/',
         views.AppRetrieveUpdateDestroyAPIViews.as_view(),
         name='app-detail'
         ),
]
