from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField

from appstore_service.apps.models import App


class AppSerializer(serializers.ModelSerializer):
    """
    Serializer for the App model,this serializer is used to convert App model 
    instances to and from JSON format.It includes fields such as 'url', 'id',
    'title',icon', 'description', 'verified', 'price', 'created_at', and
    'owner'.The 'url' field provides a hyperlink to the detailed view of the
    app.The 'owner' field is read-only and displays the first name of the app
    owner.The 'verified' and 'owner' fields are marked as read-only, meaning
    they cannot be modified through the API.

    """
    # Read-only field for the owner's first name
    owner = serializers.ReadOnlyField(source='owner.first_name')
    # Hyperlink to the app detail view
    url = HyperlinkedIdentityField(
        view_name='apps:app-detail'
    )

    # Specified the model to be serialized
    class Meta:
        model = App
        fields = [
                  'url',
                  'id',
                  'title',
                  'icon',
                  'description',
                  'verified',
                  'price',
                  'created_at',
                  'owner'
                ]
        extra_kwargs = {
            # 'verified' field is read-only
            'verified': {'read_only': True},
            # 'owner' field is read-only
            'owner': {'read_only': True},
        }
