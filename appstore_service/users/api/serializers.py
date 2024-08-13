from rest_framework import serializers

from appstore_service.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model to handle user data serialization
    and validation
    """

    # Hyperlinked field to represent related apps associated with the user
    app = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='app-detail'
    )
    # Field for confirming the user's password, used only for input
    # (write_only)
    password2 = serializers.CharField(
        label='Confirm Password', write_only=True)

    # Validate that passwords match and meet length requirements
    def validate(self, data):
        password2 = data.pop('password2')
        password = data.get('password')
        if password != password2:
            raise serializers.ValidationError("Password does not match!")
        if len(password) < 6:
            raise serializers.ValidationError(
                "Password must be at least 6 characters")
        return data

    # Create a user instance with validated data
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
     
    # Specified the model to be serialized
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2',
            'credit',
            'app'
        ]
        # Specify additional field options
        extra_kwargs = {
            # Password field is write-only
            'password': {'write_only': True},
            # Confirm password field is write-only
            'password2': {'write_only': True},
            # Credit field is read-only
            'credit': {'read_only': True},
        }
