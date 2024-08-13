# Import necessary modules and classes.
# - 'reverse' is used for reversing named URL patterns.
# - 'serializers' provides tools for serializing and deserializing data.
# - 'App' and 'Purchase' models are imported from their respective modules.

from django.urls import reverse
from rest_framework import serializers

from appstore_service.apps.models import App
from appstore_service.purchase.models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    """
    Serializer for the Purchase model.
    This serializer handles the conversion of Purchase instances to and
    from JSON format.It includes fields such as 'id', 'purchase_date', 'app',
    'unique_key', and 'app_url'.
    """
    # Custom field to generate the URL of the associated app.
    # - The 'get_app_url' method is used to generate this field.
    app_url = serializers.SerializerMethodField()

    class Meta:
        model = Purchase  # Specify the model to be serialized
        fields = [
            'id',
            'purchase_date',
            'app',
            'unique_key',
            'app_url'
        ]
        extra_kwargs = {
            # The 'purchase_date' field is read-only
            'purchase_date': {'read_only': True},
            # The 'app' field is read-only, as it references the purchased app
            'app': {'read_only': True},
        }

    # Method to generate the absolute URL for the associated app.
    # - Retrieves the request context and uses 'reverse'
    # to get the app's detail view URL.
    # - Builds an absolute URI for the app URL and returns it.
    # - Returns None if the request context is not available.
    def get_app_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            app_url = reverse('apps:app-detail', args=[obj.app.id])
            return request.build_absolute_uri(app_url)
        return None
