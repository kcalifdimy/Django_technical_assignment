from rest_framework import filters, generics, parsers, permissions

from appstore_service.apps.api.permissions import IsOwnerOrReadOnly
from appstore_service.apps.api.serializers import AppSerializer
from appstore_service.apps.models import App


class AppCreateView(generics.CreateAPIView):
    """
    View for creating a new App instance.
    Uses the CreateAPIView, which provides the logic for handling POST
    requests.The queryset includes all App instances.
    The AppSerializer is used to validate and save the data.
    FormParser and MultiPartParser are used to handle form and file upload
    data.Only authenticated users can create app
    """
    queryset = App.objects.all()
    serializer_class = AppSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [permissions.IsAuthenticated]


class AppListView(generics.ListAPIView):
    """
    View for listing all verified App instances.
    Uses the ListAPIView, which provides the logic for handling GET requests.
    The queryset is filtered to include only verified apps.
    The AppSerializer is used to serialize the app data.
    Only authenticated users can access the list of apps.
    """
    queryset = App.objects.all().filter(verified=True)
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]


class SerachView(generics.ListAPIView):
    """
    View for searching verified App instances.
    Uses the ListAPIView, similar to AppListView, but adds search 
    functionality.The queryset is filtered to include only verified apps.
    The SearchFilter is used to allow searching by 'title' and 'description'.
    Only authenticated users can perform searches.
    """
    queryset = App.objects.all().filter(verified=True)
    serializer_class = AppSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    permission_classes = [permissions.IsAuthenticated]


class AppRetrieveUpdateDestroyAPIViews(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, or deleting an App instance.
    Uses the RetrieveUpdateDestroyAPIView, which provides logic for GET, PUT,
    PATCH, and DELETE requests.The queryset includes all App instances.
    The IsOwnerOrReadOnly permission class ensures that only the owner of an
    app can update or delete it.The AppSerializer is used to serialize and
    validate the app data.
    """
    queryset = App.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AppSerializer
